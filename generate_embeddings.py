# -*- coding: utf-8 -*-
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from PIL import Image
from datetime import datetime
import requests
import io
from io import BytesIO

# === CONEXIÓN MONGODB ===
uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
client = MongoClient(uri)
db = client["homecenter"]

# === MODELOS ===

# 🔹 Modelo para embeddings de texto
from sentence_transformers import SentenceTransformer
modelo_texto = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 🔹 Modelo CLIP para embeddings de imagen y multimodales
from transformers import CLIPProcessor, CLIPModel
import torch

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# === FUNCIONES ===
def generar_embedding_texto(texto: str):
    if not texto or texto.strip() == "":
        return None
    return modelo_texto.encode(texto).tolist()

def generar_embedding_imagen(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content)).convert("RGB")
        inputs = clip_processor(images=image, return_tensors="pt")

        with torch.no_grad():
            embedding = clip_model.get_image_features(**inputs)
            return embedding.squeeze().tolist()

    except Exception as e:
        print(f"⚠️ Error cargando imagen {url}: {e}")
        return None

def generar_embedding_multimodal(texto: str, url: str):
    """Combina texto + imagen con CLIP."""
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(io.BytesIO(response.content)).convert("RGB")

        inputs = clip_processor(
            text=[texto],
            images=[img],
            return_tensors="pt",
            padding=True
        )

        with torch.no_grad():
            outputs = clip_model(**inputs)
            embedding_texto = outputs.text_embeds[0]
            embedding_imagen = outputs.image_embeds[0]

            # Puedes combinar ambos (por ejemplo, promediando)
            embedding_combinado = (embedding_texto + embedding_imagen) / 2

        return embedding_combinado.cpu().numpy().tolist()

    except Exception as e:
        print(f"⚠️ Error multimodal en {url}: {e}")
        return None


# === MAPA DE CAMPOS DE TEXTO ===
colecciones_y_campos = {
    "cliente": ["nombre", "apellido", "direccion", "correo", "telefono"],
    "sucursal": ["nombre_sucursal", "direccion", "ciudad", "descripcion"],
    "area": ["nombre_area"],
    "empleado": ["nombre", "apellido", "correo", "cargo", "direccion"],
    "producto": ["nombre_producto", "descripcion", "descripcion_larga", "marca"],
}

# === EMBEDDINGS DE TEXTO ===
# print("\n🧠 Generando embeddings de TEXTO...")
# total_texto = 0

# for nombre_col, campos in colecciones_y_campos.items():
#     for doc in db[nombre_col].find({}):
#         for campo in campos:
#             valor = doc.get(campo)
#             if not isinstance(valor, str) or valor.strip() == "":
#                 continue

#             if db.embeddings_texto.find_one({
#                 "origen": nombre_col,
#                 "id_origen": doc["_id"],
#                 "campo": campo
#             }):
#                 continue

#             emb = generar_embedding_texto(valor)
#             if not emb:
#                 continue

#             db.embeddings_texto.insert_one({
#                 "origen": nombre_col,
#                 "id_origen": doc["_id"],
#                 "campo": campo,
#                 "texto": valor,
#                 "embedding_texto": emb,
#                 "metadata": {
#                     "modelo": "all-MiniLM-L6-v2",
#                     "fecha_creacion": datetime.utcnow()
#                 }
#             })
#             total_texto += 1

# print(f"✔ {total_texto} embeddings de texto generados.")

# db.embeddings_imagen.delete_many({})
# print("🧠 Embeddings de IMAGEN eliminados para regeneración.")

# # === EMBEDDINGS DE IMÁGENES ===
# print("\n🖼 Generando embeddings de IMÁGENES...")
# total_imagen = 0

# for p in db.producto.find({}, {"_id": 1, "imagen_principal": 1, "descripcion_larga": 1}):
#     url = p.get("imagen_principal", "")
#     if not url:
#         continue

#     if db.embeddings_imagen.find_one({"producto_id": p["_id"]}):
#         continue

#     emb_img = generar_embedding_imagen(url)
#     if not emb_img:
#         continue

#     db.embeddings_imagen.insert_one({
#         "producto_id": p["_id"],
#         "imagen_url": url,
#         "embedding_imagen": emb_img,
#         "metadata": {
#             "modelo": "clip-vit-base-patch32",
#             "fecha_creacion": datetime.utcnow()
#         }
#     })
#     total_imagen += 1

# print(f"✔ {total_imagen} embeddings de imágenes generados.")

# === EMBEDDINGS MULTIMODALES ===
print("\n🎯 Generando embeddings MULTIMODALES (texto + imagen)...")
total_multi = 0

for p in db.producto.find({}, {"_id": 1, "imagen_principal": 1, "descripcion_larga": 1}):
    url = p.get("imagen_principal", "")
    texto = p.get("descripcion_larga", "")
    if not url or not texto.strip():
        continue

    if db.embeddings_imagen.find_one({
        "producto_id": p["_id"],
        "metadata.tipo": "multimodal"
    }):
        continue

    emb_multi = generar_embedding_multimodal(texto, url)
    if not emb_multi:
        continue

    db.embeddings_imagen.insert_one({
        "producto_id": p["_id"],
        "imagen_url": url,
        "embedding_imagen": emb_multi,
        "metadata": {
            "modelo": "CLIP",
            "tipo": "multimodal",
            "fecha_creacion": datetime.utcnow()
        }
    })
    total_multi += 1

print(f"✔ {total_multi} embeddings multimodales generados.")

client.close()
print("\n✅ Pipeline completo finalizado.")
