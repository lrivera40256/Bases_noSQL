# -*- coding: utf-8 -*-
# ============================================================
# GENERACIÓN DE EMBEDDINGS PARA RAG (texto + imágenes)
# ============================================================

from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import clip
import torch
from PIL import Image
import requests
from io import BytesIO
from tqdm import tqdm

# ============================================================
# CONEXIÓN A MONGO
# ============================================================

uri = "mongodb+srv://davidsuarez38528:1055752199@basesnorelacionales.gqulgyl.mongodb.net/?appName=BasesNoRelacionales"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

print("✔ Conectado a MongoDB Atlas")

# ============================================================
# MODELOS DE EMBEDDINGS
# ============================================================

print("⏳ Cargando modelo de texto (MiniLM-L6)...")
model_text = SentenceTransformer("all-MiniLM-L6-v2")

print("⏳ Cargando modelo de imágenes (CLIP ViT-B/32)...")
device = "cuda" if torch.cuda.is_available() else "cpu"
model_clip, preprocess = clip.load("ViT-B/32", device=device)

print("✔ Modelos cargados correctamente\n")

# ============================================================
# FUNCIÓN PARA GENERAR EMBEDDING DE TEXTO
# ============================================================

def generar_embedding_texto(texto):
    try:
        return model_text.encode(texto).tolist()
    except:
        return None

# ============================================================
# FUNCIÓN PARA GENERAR EMBEDDING DE IMAGEN
# ============================================================

def generar_embedding_imagen(url):
    try:
        response = requests.get(url, timeout=10)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        image = preprocess(image).unsqueeze(0).to(device)

        with torch.no_grad():
            embedding = model_clip.encode_image(image)

        return embedding.cpu().numpy().flatten().tolist()

    except Exception as e:
        print(f"⚠ Error cargando imagen {url}: {e}")
        return None

# ============================================================
# PROCESAR TODOS LOS PRODUCTOS
# ============================================================

productos = list(db.producto.find({}))
print(f"🔍 Productos encontrados: {len(productos)}\n")

for producto in tqdm(productos, desc="Generando embeddings"):

    descripcion_larga = producto.get("descripcion_larga", "")
    imagen_url = producto.get("imagen_principal", None)

    # Embedding de texto
    emb_texto = generar_embedding_texto(descripcion_larga)

    # Embedding de imagen
    emb_imagen = generar_embedding_imagen(imagen_url) if imagen_url else None

    # Documento para colección embeddings
    doc = {
        "origen": "producto",
        "id_origen": producto["_id"],
        "texto": descripcion_larga,
        "embedding_texto": emb_texto,
        "imagen_url": imagen_url,
        "embedding_imagen": emb_imagen,
        "metadata": {
            "categoria": producto["categoria"]["nombre_categoria_producto"],
            "marca": producto["marca"],
            "precio": producto["precio"]
        }
    }

    db.embeddings.insert_one(doc)

print("\n🎉 Embeddings generados y almacenados correctamente.")
client.close()
