import time
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from test_chunks import chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

# question = "How was speech converted into notes?"
question = "What database was used?"

question_embedding = model.encode(question)

print(f"\nQuestion: {question}\n")

start = time.time()

chunk_embeddings = []

for chunk in chunks:
    embedChunk = model.encode(chunk)
    similarity = cos_sim(
        question_embedding,
        embedChunk
    )
    chunk_embeddings.append({
        "text": chunk,
        "embedding": embedChunk,
        "simialrity": similarity,
    })

sorted_chunks = sorted(chunk_embeddings, key=lambda x: x["simialrity"], reverse=True)

top_k = 5
top_chunks = sorted_chunks[:top_k]

context = "\n\n".join(
    chunk["text"]
    for chunk in top_chunks
)

end = time.time()

print(context)

print(f"\nManual retrieval time: {end - start:.4f} seconds")