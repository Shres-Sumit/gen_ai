from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences =  [
    "The cat sat on the mat.",
    "A dog is playing in the park.",
    "I love eating pizza on weekends.",
    "The feline rested peacefully on the rug.",
    "Machine learning models learn patterns from data."
]

embeddings = model.encode(sentences)

def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

print("Comparing sentence 1 ('cat sat on mat') to all others:\n")
for i in range(1, len(sentences)):
    sim = cosine_similarity(embeddings[0], embeddings[i])
    print(f"vs \"{sentences[i]}\"  ->  similarity: {sim:.4f}")