# Crear índice vectorial para búsqueda por imagen en MongoDB Atlas

## 1. Acceder a MongoDB Atlas

1. Ve a https://cloud.mongodb.com
2. Navega a tu cluster "student"
3. Ve a la base de datos "homecenter"
4. Selecciona la colección "embeddings_imagen"

## 2. Crear Atlas Search Index

1. Click en la pestaña "Search Indexes"
2. Click en "Create Index"
3. Selecciona "JSON Editor"
4. Pega la siguiente configuración:

```json
{
  "name": "imagen_index",
  "type": "vectorSearch",
  "fields": [
    {
      "type": "vector",
      "path": "embedding_imagen",
      "numDimensions": 512,
      "similarity": "cosine"
    },
    {
      "type": "filter",
      "path": "producto_id"
    },
    {
      "type": "filter",
      "path": "metadata.tipo"
    }
  ]
}
```

5. Click en "Next"
6. Confirma el nombre del índice: **imagen_index**
7. Click en "Create Search Index"
8. Espera a que el índice termine de construirse (status: "Active")

## 3. Verificar índice

El índice debe tener:

- **Nombre**: `imagen_index`
- **Tipo**: Vector Search
- **Dimensiones**: 512 (CLIP)
- **Similarity**: cosine
- **Path**: `embedding_imagen`

## 4. Verificar datos

Asegúrate de tener embeddings de imagen en la colección:

```javascript
// En MongoDB Compass o Shell
db.embeddings_imagen.countDocuments();
// Debe retornar > 0

// Ver un ejemplo
db.embeddings_imagen.findOne();
```

El documento debe tener esta estructura:

```json
{
  "_id": ObjectId("..."),
  "producto_id": ObjectId("..."),
  "imagen_url": "https://drive.google.com/...",
  "embedding_imagen": [0.123, -0.456, ...],  // Array de 512 números
  "metadata": {
    "modelo": "CLIP",
    "tipo": "multimodal",
    "fecha_creacion": ISODate("...")
  }
}
```

## 5. Prueba el índice

Una vez creado, prueba desde tu aplicación:

```bash
# Reinicia el servidor
uvicorn app:app --reload --port 8000
```

Luego en el navegador:

1. Abre http://localhost:8000/static/client.html
2. En `/search`, sube una imagen o pega una URL
3. Debe retornar productos similares visualmente

## Troubleshooting

**Error: "index not found"**
→ El índice aún no terminó de construirse. Espera unos minutos.

**Error: "no documents match"**
→ Verifica que existan embeddings: `db.embeddings_imagen.countDocuments()`

**Error: "dimensions mismatch"**
→ Verifica que los embeddings tengan 512 dimensiones:

```javascript
db.embeddings_imagen.findOne({}, { embedding_imagen: 1 });
// Cuenta el tamaño del array
```

## Nota importante

Si no has generado los embeddings de imagen aún, ejecuta:

```bash
python generate_embeddings.py
```

Esto generará los embeddings multimodales (texto + imagen) usando CLIP.
