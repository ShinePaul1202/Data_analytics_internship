
from pathlib import Path
import numpy as np
import pandas as pd
import torch

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)

# --------------------------------------------------
# Locate the dataset
# --------------------------------------------------

def find_file(name):
    search_roots = [
        Path("/kaggle/input"),
        Path("/content"),
        Path(__file__).resolve().parent / "dataset"
        if "__file__" in globals()
        else Path("dataset"),
        Path(".")
    ]

    for root in search_roots:
        if root.exists():
            matches = sorted(root.rglob(name))
            if matches:
                return matches[0]

    raise FileNotFoundError(
        f"Could not find {name}. Attach the Kaggle dataset "
        "or place the file in the dataset folder."
    )


fake_path = find_file("Fake.csv")
true_path = find_file("True.csv")

print("Fake dataset:", fake_path)
print("Real dataset:", true_path)

BASE_DIR = (
    Path(__file__).resolve().parent
    if "__file__" in globals()
    else Path.cwd()
)

# --------------------------------------------------
# Check hardware
# --------------------------------------------------

use_gpu = torch.cuda.is_available()

print("PyTorch version:", torch.__version__)
print("GPU available:", use_gpu)

# Use the full dataset on GPU.
# Limit the sample size on CPU to reduce training time.
SAMPLE_SIZE = None if use_gpu else 6000

# --------------------------------------------------
# Load and prepare the data
# --------------------------------------------------

fake_df = pd.read_csv(fake_path)
true_df = pd.read_csv(true_path)

# Labels: 0 = Fake, 1 = Real
fake_df["label"] = 0
true_df["label"] = 1

df = pd.concat(
    [fake_df, true_df],
    ignore_index=True
)

# Use headlines as the input text
df = df[["title", "label"]].dropna()

df["title"] = df["title"].astype(str).str.strip()
df = df[df["title"] != ""]

# Remove exact duplicate headlines
df = df.drop_duplicates(subset="title").reset_index(drop=True)

if SAMPLE_SIZE is not None and len(df) > SAMPLE_SIZE:
    df = df.sample(
        n=SAMPLE_SIZE,
        random_state=42
    ).reset_index(drop=True)

print("\nDataset size:", len(df))
print("\nClass distribution:")
print(df["label"].value_counts().sort_index())

# --------------------------------------------------
# Split into training, validation and test sets
# --------------------------------------------------

train_val_texts, test_texts, y_train_val, y_test = train_test_split(
    df["title"].tolist(),
    df["label"].tolist(),
    test_size=0.20,
    random_state=42,
    stratify=df["label"]
)

train_texts, val_texts, y_train, y_val = train_test_split(
    train_val_texts,
    y_train_val,
    test_size=0.125,
    random_state=42,
    stratify=y_train_val
)

# This gives approximately 70% training, 10% validation,
# and 20% testing.

print("\nTraining examples:", len(train_texts))
print("Validation examples:", len(val_texts))
print("Test examples:", len(test_texts))

# --------------------------------------------------
# Tokenize headlines
# --------------------------------------------------

model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)

train_enc = tokenizer(
    train_texts,
    truncation=True,
    max_length=64
)

val_enc = tokenizer(
    val_texts,
    truncation=True,
    max_length=64
)

test_enc = tokenizer(
    test_texts,
    truncation=True,
    max_length=64
)

# --------------------------------------------------
# Create PyTorch Dataset
# --------------------------------------------------

class NewsDataset(torch.utils.data.Dataset):

    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        item = {
            key: torch.tensor(value[index], dtype=torch.long)
            for key, value in self.encodings.items()
        }

        item["labels"] = torch.tensor(
            int(self.labels[index]),
            dtype=torch.long
        )

        return item


train_ds = NewsDataset(train_enc, y_train)
val_ds = NewsDataset(val_enc, y_val)
test_ds = NewsDataset(test_enc, y_test)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# --------------------------------------------------
# Load pretrained BERT for classification
# --------------------------------------------------

model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=2,
    id2label={0: "FAKE", 1: "REAL"},
    label2id={"FAKE": 0, "REAL": 1}
)

# --------------------------------------------------
# Define evaluation metrics
# --------------------------------------------------

def compute_metrics(eval_pred):
    logits, labels = eval_pred

    predictions=np.argmax(logits, axis=-1)

    return {
        "accuracy": accuracy_score(labels, predictions),
        "f1_fake": f1_score(
            labels, predictions, pos_label=0, zero_division=0
        ),
        "f1_real": f1_score(
            labels, predictions, pos_label=1, zero_division=0
        ),
        "f1_macro": f1_score(
            labels, predictions, average="macro", zero_division=0
        )
    }

# --------------------------------------------------
# Configure training
# --------------------------------------------------

training_args = TrainingArguments(
    output_dir=str(BASE_DIR / "bert_fake_news_results"),
    num_train_epochs=1,
    per_device_train_batch_size=16 if use_gpu else 8,
    per_device_eval_batch_size=32 if use_gpu else 8,
    eval_strategy="epoch",
    save_strategy="no",
    logging_steps=50,
    fp16=use_gpu,
    dataloader_pin_memory=use_gpu,
    report_to="none",
    seed=42
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

# --------------------------------------------------
# Fine-tune BERT
# --------------------------------------------------

print("\nStarting BERT fine-tuning...")
trainer.train()

# --------------------------------------------------
# Evaluate on the held-out test set
# --------------------------------------------------

print("\nEvaluating on the test set...")

test_output = trainer.predict(test_ds)

test_predictions = np.argmax(
    test_output.predictions,
    axis=-1
)

print("\nTest Results")
print("-" * 40)

print(
    "Accuracy:",
    f"{accuracy_score(y_test, test_predictions):.4f}"
)

print(
    "Fake News F1:",
    f"{f1_score(y_test, test_predictions, pos_label=0, zero_division=0):.4f}"
)

print(
    "Real News F1:",
    f"{f1_score(y_test, test_predictions, pos_label=1, zero_division=0):.4f}"
)

print(
    "Macro F1:",
    f"{f1_score(y_test, test_predictions, average='macro', zero_division=0):.4f}"
)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        test_predictions,
        labels=[0, 1],
        target_names=["FAKE", "REAL"],
        zero_division=0
    )
)

# --------------------------------------------------
# Predict the required unseen headlines
# --------------------------------------------------

test_headlines = [
    "NASA confirms second moon to be visible till 2083.",
    "Aliens built the pyramids, claims new study"
]

model.eval()

headline_encodings = tokenizer(
    test_headlines,
    truncation=True,
    padding=True,
    max_length=64,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
    logits = model(**headline_encodings).logits
    probabilities = torch.softmax(logits, dim=-1).cpu().numpy()

print("\nUnseen Headline Predictions")
print("-" * 40)

for headline, probs in zip(test_headlines, probabilities):
    predicted_label = int(np.argmax(probs))
    category = "REAL" if predicted_label == 1 else "FAKE"
    confidence = float(probs[predicted_label])

    print(f"\nHeadline: {headline}")
    print(f"Predicted category: {category}")
    print(f"Confidence: {confidence:.4f}")

# --------------------------------------------------
# Save the fine-tuned model
# --------------------------------------------------

model_dir=BASE_DIR / "fine_tuned_bert"

trainer.save_model(str(model_dir))
tokenizer.save_pretrained(str(model_dir))

print(f"\nFine-tuned model saved to: {model_dir}")
print("Task 5 completed successfully.")
