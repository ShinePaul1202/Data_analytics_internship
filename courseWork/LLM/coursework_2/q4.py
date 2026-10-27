
import torch
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import AutoTokenizer, AutoModel

# Sentence given in the coursework
sentence = (
    "Peacock is the national bird of India. "
    "It can be seen only in a few states of the country"
)

# Load pretrained BERT and its tokenizer
model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(
    model_name,
    attn_implementation="eager"
)

model.eval()

# Tokenize the sentence
inputs = tokenizer(sentence, return_tensors="pt")

tokens = tokenizer.convert_ids_to_tokens(
    inputs["input_ids"][0]
)

# Obtain attention weights without calculating gradients
with torch.no_grad():
    outputs = model(
        **inputs,
        output_attentions=True
    )

# Layer 1 attention:
# Shape before averaging: (heads, tokens, tokens)
layer1_attention = outputs.attentions[0][0]

# Average attention across all heads
attention = layer1_attention.mean(dim=0).numpy()

# Display token attention heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(
    attention,
    xticklabels=tokens,
    yticklabels=tokens,
    cmap="viridis"
)
plt.title("BERT Layer 1 Self-Attention (Average Across Heads)")
plt.xlabel("Key Tokens (tokens being attended to)")
plt.ylabel("Query Tokens (tokens attending)")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("q4_attention_heatmap.png", dpi=300)
plt.show()

# Find token positions, ignoring special tokens
def find_token_position(word):
    word = word.lower()

    for i, token in enumerate(tokens):
        clean_token = token.replace("##", "")

        if clean_token == word:
            return i

    raise ValueError(f"Token '{word}' not found: {tokens}")

# Print the requested attention scores
pairs = [
    ("It", "Peacock"),
    ("bird", "Peacock"),
    ("India", "country")
]

print("\nLayer 1 Attention Scores (averaged across heads):")

for query_word, key_word in pairs:
    query_idx = find_token_position(query_word)
    key_idx = find_token_position(key_word)

    score = attention[query_idx, key_idx]

    print(
        f"Attention from '{query_word}' to '{key_word}': "
        f"{score:.6f}"
    )

print("\nHeatmap saved as q4_attention_heatmap.png")
