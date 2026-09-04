from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "The cat sat on the mat.",
    "A dog is playing in the park.",
    "I love eating pizza on weekends.",
    "The feline rested peacefully on the rug.",
    "Machine learning models learn patterns from data."
]

sentence_embeddings = model.encode(sentences)

query = "Where is the kitten sitting?"
query_embedding = model.encode(query)

similarities = util.cos_sim(query_embedding, sentence_embeddings)[0] 

print(f"Query: \"{query}\"\n")
for sentence, score in zip(sentences, similarities):
    print(f"{score:.4f}  ->  {sentence}")


ranked = sorted(zip(sentences, similarities.tolist()), key=lambda x: x[1], reverse=True)

print(f"\nRanked results for: \"{query}\"\n")
for rank, (sentence, score) in enumerate(ranked, start=1):
    print(f"{rank}. ({score:.4f}) {sentence}")    