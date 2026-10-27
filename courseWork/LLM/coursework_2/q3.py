
from pathlib import Path
from transformers import pipeline

# Locate the Articles folder
BASE_DIR = Path(__file__).resolve().parent
ARTICLES_DIR = BASE_DIR / "Articles"

# Load the pretrained NER pipeline
ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

# Entity labels to extract
wanted_labels = {"PER", "ORG", "LOC"}

# Process every text article
for file_path in sorted(ARTICLES_DIR.glob("*.txt")):
    text = file_path.read_text(encoding="utf-8").strip()

    if not text:
        print(f"\nSkipping empty file: {file_path.name}")
        continue

    entities = ner(text)

    print(f"\nArticle: {file_path.name}")
    print("-" * 40)

    found = False

    for entity in entities:
        label = entity["entity_group"]

        if label in wanted_labels:
            print(f"{label}: {entity['word']}")
            found = True

    if not found:
        print("No people, organizations, or locations found.")

print("\nNamed entity extraction completed.")
