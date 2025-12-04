from fastapi import FastAPI, Body
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from bson import ObjectId

app = FastAPI()

# === Conexión a MongoDB ===
client = MongoClient("mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student")
db = client["homecenter"]

# === Modelo para consultas ===
modelo_texto = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

@app.post("/search")
async def search(request: dict = Body(...)):
    query = request["query"]
    embedding = modelo_texto.encode(query).tolist()

    # 1️⃣ Búsqueda vectorial
    base_results = list(db.embeddings_texto.aggregate([
        {
            "$vectorSearch": {
                "index": "vector_index",               # <-- tu índice real
                "path": "embedding_texto",             # <-- tu campo real
                "queryVector": embedding,
                "numCandidates": 200,
                "limit": 10
            }
        },
        {
            "$project": {
                "_id": 1,
                "id_origen": 1,
                "origen": 1,
                "campo": 1,
                "texto": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]))

    # 2️⃣ Enriquecer los resultados (solo productos)
    for doc in base_results:
        if doc["origen"] == "producto":
            prod = db.producto.find_one(
                {"_id": doc["id_origen"]},
                {"nombre_producto": 1, "marca": 1}
            )
            if prod:
                doc["producto"] = prod

    return base_results
