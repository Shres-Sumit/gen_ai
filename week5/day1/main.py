from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "The cat sat on the mat.",
    "A dog is playing in the park.",
    "I love eating pizza on weekends.",
    "The feline rested peacefully on the rug.",
    "Machine learning models learn patterns from data."
]

embeddings = model.encode(sentences)

print("Number of sentences:", len(sentences))
print("Shape of embeddings:", embeddings.shape)  # (5, 384)
print("\nFirst 10 numbers of sentence 1's vector:")
print(embeddings[0][:10])