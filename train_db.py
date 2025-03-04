import chromadb
from sentence_transformers import SentenceTransformer

# Load model embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load database vektor
chroma_client = chromadb.PersistentClient(path="./knowledge_db")
collection = chroma_client.get_or_create_collection(name="knowledge")

# Baca file knowledge.txt
with open("knowledge/knowledge.txt", "r", encoding="utf-8") as f:
    texts = f.readlines()

# Tambahkan ke database
for idx, text in enumerate(texts):
    embedding = model.encode(text).tolist()
    collection.add(ids=[str(idx)], embeddings=[embedding], documents=[text])

print("Database pengetahuan berhasil dibuat!")
