from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from bson import ObjectId
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = FastAPI()

groq_client = Groq(api_key=GROQ_API_KEY)

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
                "index": "vector_index",
                "path": "embedding_texto",
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

    # 🧩 Conversión segura antes del retorno
    return jsonable_encoder(
        base_results,
        custom_encoder={ObjectId: str}
    )

@app.post("/rag")
async def rag(request: dict = Body(...)):
    query = request["query"]

    # → Crear embedding
    embedding = modelo_texto.encode(query).tolist()

    # → Recuperar contexto relevante
    retrieved = list(db.embeddings_texto.aggregate([
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding_texto",
                "queryVector": embedding,
                "numCandidates": 200,
                "limit": 5
            }
        },
        {
            "$project": {
                "_id": 0,
                "texto": 1,
                "origen": 1,
                "campo": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]))

    # → Convertir documentos a texto plano para el LLM
    context_text = "\n".join([f"- ({d['origen']}.{d['campo']}): {d['texto']}" for d in retrieved])

    if context_text.strip() == "":
        context_text = "No se encontró contexto relevante en la base de datos."

    # → Construir prompt RAG
    prompt = f"""
Eres un asistente experto. Responde la siguiente pregunta utilizando SOLO el contexto proporcionado.

### CONTEXTO:
{context_text}

### PREGUNTA:
{query}

### RESPUESTA:
"""

    # → Llamar al modelo Groq Llama 3.1
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Eres un experto en razonamiento y respuestas basadas en contexto."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content

    return {
        "query": query,
        "context_used": retrieved,
        "answer": answer
    }