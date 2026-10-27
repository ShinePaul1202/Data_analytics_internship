
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.optim import AdamW

# --------------------------------------------------
# Prepare the dataset
# --------------------------------------------------

texts = [
    "I love this product!",
    "It was terrible.",
    "The service was great.",
    "Not happy with the movie.",
    "Fantastic experience!"
]

labels = [1, 0, 1, 0, 1]  # 1 = positive, 0 = negative

# --------------------------------------------------
# Load the pretrained DistilBERT tokenizer
# --------------------------------------------------

model_name = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)

encodings=tokenizer(
    texts,
    truncation=True,
    padding=True,
    max_length=128,
    return_tensors="pt"
)

print("Tokenization completed.")
print("Input IDs shape:", encodings["input_ids"].shape)

# --------------------------------------------------
# Create a PyTorch Dataset
# --------------------------------------------------

class SentimentDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        item={
            key: value[index]
            for key, value in self.encodings.items()
        }
        item["labels"] = self.labels[index]
        return item


dataset = SentimentDataset(encodings, labels)

# --------------------------------------------------
# Create a DataLoader
# --------------------------------------------------

dataloader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

print("DataLoader created.")
print("Number of batches:", len(dataloader))

# --------------------------------------------------
# Load the pretrained DistilBERT model
# --------------------------------------------------

model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=2
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("Device:", device)

# --------------------------------------------------
# Fine-tune the model for one epoch
# --------------------------------------------------

optimizer = AdamW(model.parameters(), lr=2e-5)

model.train()
total_loss = 0

for batch in dataloader:
    batch = {
        key: value.to(device)
        for key, value in batch.items()
    }

    optimizer.zero_grad()

    outputs = model(**batch)
    loss = outputs.loss

    loss.backward()
    optimizer.step()

    total_loss+=loss.item()

average_loss = total_loss / len(dataloader)

print("\nTraining completed.")
print("Epochs: 1")
print(f"Average training loss: {average_loss:.4f}")

# --------------------------------------------------
# Evaluate accuracy
# --------------------------------------------------

model.eval()

correct = 0
total = 0

with torch.no_grad():
    for batch in dataloader:
        batch = {
            key: value.to(device)
            for key, value in batch.items()
        }

        labels_batch = batch["labels"]
        outputs = model(**batch)

        predictions = torch.argmax(outputs.logits, dim=1)

        correct += (predictions == labels_batch).sum().item()
        total += labels_batch.size(0)

accuracy = correct / total

print(f"\nTraining-set accuracy: {accuracy:.4f}")
print(f"Training-set accuracy percentage: {accuracy * 100:.2f}%")

# --------------------------------------------------
# Show predictions
# --------------------------------------------------

print("\nSentiment Predictions:")

with torch.no_grad():
    for text in texts:
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True
        ).to(device)

        outputs=model(**inputs)
        prediction=torch.argmax(outputs.logits, dim=1).item()

        sentiment="Positive" if prediction == 1 else "Negative"

        print(f"Text: {text}")
        print(f"Predicted sentiment: {sentiment}\n")
