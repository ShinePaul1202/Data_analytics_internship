
from pathlib import Path
from transformers import pipeline

# Folder containing the text reports
BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "WeeklyTrends"

# Load the summarization pipeline
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

# Read and summarize every text file
for file_path in sorted(REPORT_DIR.glob("*.txt")):
    text = file_path.read_text(encoding="utf-8").strip()

    if not text:
        print(f"\nSkipping empty file: {file_path.name}")
        continue

    result = summarizer(
        text,
        max_length=100,
        min_length=25,
        do_sample=False,
        truncation=True
    )

    print(f"\nReport: {file_path.name}")
    print("Summary:", result[0]["summary_text"])

print("\nSummarization completed.")
