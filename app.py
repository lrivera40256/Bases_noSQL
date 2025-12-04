from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from bson import ObjectId
from groq import Groq
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import os
import requests
import base64
import re
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = FastAPI()
groq_client = Groq(api_key=GROQ_API_KEY)

# Permitir CORS desde el cliente estático (útil durante desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

client = MongoClient("mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student")
db = client["homecenter"]

modelo_texto = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def convert_image_url_to_base64(url: str) -> str:
    """
    Descarga una imagen desde una URL y la convierte a base64 data URI.
    Maneja específicamente URLs de Google Drive.
    """
    try:
        # Convertir URL de Google Drive al formato de descarga directa
        if 'drive.google.com' in url:
            # Extraer ID del archivo
            import re
            match = re.search(r'[?&]id=([^&]+)', url)
            if match:
                file_id = match.group(1)
                # Usar formato de thumbnail que funciona mejor
                download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
            else:
                download_url = url
        else:
            download_url = url
        
        # Descargar la imagen
        response = requests.get(download_url, timeout=10)
        response.raise_for_status()
        
        # Detectar el tipo MIME de la imagen
        content_type = response.headers.get('content-type', 'image/jpeg')
        
        # Convertir a base64
        image_base64 = base64.b64encode(response.content).decode('utf-8')
        
        # Retornar como data URI
        return f"data:{content_type};base64,{image_base64}"
    
    except Exception as e:
        print(f"Error al convertir imagen {url}: {e}")
        return url

def load_image_from_input(image_input: str) -> Image.Image:
    """
    Carga una imagen desde base64 data URI o URL.
    Retorna un objeto PIL Image.
    """
    try:
        # Si es data URI base64
        if image_input.startswith('data:image'):
            # Extraer la parte base64
            base64_data = image_input.split(',', 1)[1]
            image_bytes = base64.b64decode(base64_data)
            return Image.open(BytesIO(image_bytes)).convert('RGB')
        
        # Si es URL
        elif image_input.startswith('http'):
            # Manejar URLs de Google Drive
            if 'drive.google.com' in image_input:
                match = re.search(r'[?&]id=([^&]+)', image_input)
                if match:
                    file_id = match.group(1)
                    download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
                else:
                    download_url = image_input
            else:
                download_url = image_input
            
            response = requests.get(download_url, timeout=10)
            response.raise_for_status()
            return Image.open(BytesIO(response.content)).convert('RGB')
        
        else:
            raise ValueError("Formato de imagen no soportado. Use data URI o URL http(s).")
    
    except Exception as e:
        raise ValueError(f"Error al cargar imagen: {e}")

def get_image_embedding(image_input: str) -> list:
    """
    Genera embedding vectorial de una imagen usando CLIP (512 dimensiones).
    Compatible con la colección embeddings_imagen.
    """
    image = load_image_from_input(image_input)
    inputs = clip_processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        embedding = clip_model.get_image_features(**inputs)
        return embedding.squeeze().tolist()

@app.post("/search")
async def search(request: dict = Body(...)):
    query = request.get("query")
    image_input = request.get("image")
    
    if not query and not image_input:
        return {"error": "Debe proporcionar 'query' (texto) o 'image' (base64/URL)"}
    
    if image_input:
        try:
            embedding = get_image_embedding(image_input)
            search_type = "imagen"
            collection_name = "embeddings_imagen"
            embedding_field = "embedding_imagen"
            index_name = "imagen_index"
        except Exception as e:
            return {"error": f"Error al procesar imagen: {str(e)}"}
    else:
        embedding = modelo_texto.encode(query).tolist()
        search_type = "texto"
        collection_name = "embeddings_texto"
        embedding_field = "embedding_texto"
        index_name = "vector_index"

    base_results = list(db[collection_name].aggregate([
        {
            "$vectorSearch": {
                "index": index_name,
                "path": embedding_field,
                "queryVector": embedding,
                "numCandidates": 200,
                "limit": 10
            }
        },
        {
            "$project": {
                "_id": 1,
                "producto_id": 1,
                "id_origen": 1,
                "origen": 1,
                "campo": 1,
                "texto": 1,
                "imagen_url": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]))

    for doc in base_results:
        product_id = doc.get("producto_id") or doc.get("id_origen")
        
        if product_id and isinstance(product_id, ObjectId):
            prod = db.producto.find_one(
                {"_id": product_id},
                {"nombre_producto": 1, "marca": 1, "imagen_principal": 1, "descripcion": 1}
            )
            if prod:
                prod["_id"] = str(prod["_id"])
                
                if prod.get("imagen_principal"):
                    prod["imagen_principal"] = convert_image_url_to_base64(prod["imagen_principal"])
                
                doc["producto"] = prod
        
        if doc.get("producto_id"):
            doc["producto_id"] = str(doc["producto_id"])
        if doc.get("id_origen"):
            doc["id_origen"] = str(doc["id_origen"])

    return jsonable_encoder(
        {
            "search_type": search_type,
            "query": query if query else None,
            "image_provided": bool(image_input),
            "results": base_results
        },
        custom_encoder={ObjectId: str}
    )


@app.post("/rag")
async def rag(request: dict = Body(...)):
    query = request.get("query")
    image_input = request.get("image")
    
    if not query:
        return {"error": "El campo 'query' (texto) es obligatorio para RAG"}

    if image_input:
        try:
            embedding = get_image_embedding(image_input)
            search_type = "imagen + texto"
            collection_name = "embeddings_imagen"
            embedding_field = "embedding_imagen"
            index_name = "imagen_index"
        except Exception as e:
            return {"error": f"Error al procesar imagen: {str(e)}"}
    else:
        embedding = modelo_texto.encode(query).tolist()
        search_type = "texto"
        collection_name = "embeddings_texto"
        embedding_field = "embedding_texto"
        index_name = "vector_index"

    retrieved = list(db[collection_name].aggregate([
        {
            "$vectorSearch": {
                "index": index_name,
                "path": embedding_field,
                "queryVector": embedding,
                "numCandidates": 200,
                "limit": 5
            }
        },
        {
            "$project": {
                "_id": 0,
                "producto_id": 1,
                "id_origen": 1,
                "texto": 1,
                "origen": 1,
                "campo": 1,
                "imagen_url": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]))

    for d in retrieved:
        product_id = d.get("producto_id") or d.get("id_origen")
        
        if product_id and isinstance(product_id, ObjectId):
            prod = db.producto.find_one(
                {"_id": product_id},
                {"nombre_producto": 1, "marca": 1, "imagen_principal": 1, "descripcion": 1}
            )
            if prod:
                prod["_id"] = str(prod["_id"])
                
                if prod.get("imagen_principal"):
                    prod["imagen_principal"] = convert_image_url_to_base64(prod["imagen_principal"])
                
                d["producto"] = prod
        
        if d.get("producto_id"):
            d["producto_id"] = str(d["producto_id"])
        if d.get("id_origen"):
            d["id_origen"] = str(d["id_origen"])

    context_parts = []
    for d in retrieved:
        if d.get("texto"):
            context_parts.append(f"- ({d.get('origen', 'producto')}.{d.get('campo', 'info')}): {d['texto']}")
        elif d.get("producto"):
            p = d["producto"]
            context_parts.append(f"- Producto: {p.get('nombre_producto')} - {p.get('descripcion', 'Sin descripción')}")
    
    context_text = "\n".join(context_parts) or "No se encontró contexto relevante en la base de datos."

    prompt = f"""
    Eres un asistente experto en productos, servicios y categorías de Homecenter.
    Tu tarea es responder de forma precisa, útil y clara a la siguiente pregunta del usuario,
    utilizando EXCLUSIVAMENTE la información disponible en el contexto proporcionado.

    INSTRUCCIONES:
    - No inventes ni asumas información que no aparezca explícitamente en el contexto.
    - Si el contexto no contiene la respuesta, di amablemente que no se encontró información suficiente.
    - Usa un lenguaje natural, breve y profesional.
    - Si el contexto incluye varios productos o coincidencias, menciona los más relevantes.
    - Puedes incluir nombres de productos, marcas, descripciones o categorías si ayudan a responder.

    ### CONTEXTO (información recuperada desde la base de datos NoSQL de Homecenter):
    {context_text}

    ### PREGUNTA DEL USUARIO:
    {query}

    ### RESPUESTA:
    """

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Eres un experto en razonamiento y respuestas basadas en contexto."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    answer = response.choices[0].message.content

    return jsonable_encoder(
        {
            "search_type": search_type,
            "query": query,
            "image_provided": bool(image_input),
            "context_used": retrieved,
            "answer": answer
        },
        custom_encoder={ObjectId: str}
    )