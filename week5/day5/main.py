
from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "The cat sat on the mat.",
    "A dog is playing in the park.",
    "I love eating pizza on weekends.",
    "The feline rested peacefully on the rug.",
    "Machine learning models learn patterns from data."
]

def build_index(sentence_list):
    embeddings = model.encode(sentence_list)
    return {"sentences": sentence_list, "embeddings": embeddings}

def semantic_search(query, index, top_k=1):
    query_embedding = model.encode(query)
    similarities = util.cos_sim(query_embedding, index["embeddings"])[0]
    ranked = sorted(
        zip(index["sentences"], similarities.tolist()),
        key=lambda x: x[1],
        reverse=True
    )
    return ranked[:top_k]

index = build_index(sentences)


test_queries = [
    "Where is the kitten sitting?",         
    "A puppy running around outside.",        
    "What food do people eat on Saturdays?", 
    "Neural networks trained on datasets.",   
    "What time does the store close?",       
    "The mat sat on the cat.",               
]

results_log = []
for query in test_queries:
    best_sentence, best_score = semantic_search(query, index, top_k=1)[0]
    results_log.append({
        "query": query,
        "best_match": best_sentence,
        "score": round(best_score, 4)
    })

df = pd.DataFrame(results_log)
print(df.to_string(index=False))