
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "The cat sat on the mat.",
    "A dog is playing in the park.",
    "I love eating pizza on weekends.",
    "The feline rested peacefully on the rug.",
    "Machine learning models learn patterns from data."
]


def build_index(sentence_list):
    """Embed the dataset once. Returns sentences + their embeddings together."""
    embeddings = model.encode(sentence_list)
    return {"sentences": sentence_list, "embeddings": embeddings}


def semantic_search(query, index, top_k=1):
    """Embed the query, compare against the index, return top_k matches."""
    query_embedding = model.encode(query)
    similarities = util.cos_sim(query_embedding, index["embeddings"])[0]

    ranked = sorted(
        zip(index["sentences"], similarities.tolist()),
        key=lambda x: x[1],
        reverse=True
    )
    return ranked[:top_k]


index = build_index(sentences)

query = "Where is the kitten sitting?"
results = semantic_search(query, index, top_k=1)

best_sentence, best_score = results[0]
print(f"Query: \"{query}\"")
print(f"Best match: \"{best_sentence}\"  (score: {best_score:.4f})")