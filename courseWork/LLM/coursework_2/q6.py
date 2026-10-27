
import re
import torch
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# --------------------------------------------------
# text block
# --------------------------------------------------

text = """
There are two types of jungle safari available in Bandhavgarh National Park,
Jeep Safari and Elephant Safari but currently Elephant safari is not operational
in Bandhavgarh Tiger Reserve. Although there are severe restrictions on who may
go and when. Only a certain number of vehicles are permitted on safaris at each
departure time, which makes it crucial that you make reservations in advance to
guarantee your spot. Safari timings and capacity depends on the season and forest
authority. The reservation fee includes your park entry permit. It is not permitted
to enter the park on your own; visitors must arrive with a guide and an approved
vehicle. The tentative safari timings are given below in the table.
"""

# --------------------------------------------------
# Generate five questions
# --------------------------------------------------

question_generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

prompt = f"""
Generate exactly five different factual questions based only on the
following passage. Cover different facts and do not repeat questions.
Return one question per line.

Passage:
{text}
"""

result = question_generator(
    prompt,
    max_new_tokens=150,
    do_sample=False
)

generated_text = result[0]["generated_text"]

questions = []

for line in generated_text.splitlines():
    line = re.sub(r"^\s*[\d\-*.)]+\s*", "", line).strip()

    if line and "?" in line:
        question = line[:line.index("?") + 1]

        if question.lower() not in [q.lower() for q in questions]:
            questions.append(question)

# Use five distinct questions if the model does not return five.
if len(questions) < 5:
    questions = [
        "What are the two types of jungle safari available?",
        "Why should visitors make reservations in advance?",
        "What determines safari timings and capacity?",
        "What does the reservation fee include?",
        "What must visitors have to enter the park?"
    ]

questions = questions[:5]

print("\nGenerated Questions:")
for i, question in enumerate(questions, start=1):
    print(f"Q{i}: {question}")

# --------------------------------------------------
# Divide the text into sentences
# --------------------------------------------------

sentences = [
    sentence.strip()
    for sentence in re.split(r"(?<=[.!?])\s+", text.strip())
    if sentence.strip()
]

print("\nSentences:")
for i, sentence in enumerate(sentences, start=1):
    print(f"S{i}: {sentence}")

# --------------------------------------------------
# Encode sentences using a transformer model
# --------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence_embeddings = model.encode(
    sentences,
    convert_to_tensor=True
)

# --------------------------------------------------
# Retrieve the most relevant sentence
# --------------------------------------------------

print("\nAnswers to Generated Questions:")

for i, question in enumerate(questions, start=1):

    question_embedding = model.encode(
        question,
        convert_to_tensor=True
    )

    similarity_scores = util.cos_sim(
        question_embedding,
        sentence_embeddings
    )[0]

    best_index = torch.argmax(similarity_scores).item()
    best_sentence = sentences[best_index]
    best_score = similarity_scores[best_index].item()

    print(f"\nQ{i}: {question}")
    print(f"Most Relevant Sentence: {best_sentence}")
    print(f"Similarity Score: {best_score:.4f}")
