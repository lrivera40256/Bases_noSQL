from pymongo import MongoClient
from bson import ObjectId
import random
from datetime import datetime, timedelta

uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

# =============================
# 1. Obtener IDs reales
# =============================

productos = list(db.producto.find({}, {"_id": 1}))
sucursales = list(db.sucursal.find({}, {"_id": 1}))

if not productos:
    print("❌ No existen productos. Inserta productos primero.")
    exit()

if not sucursales:
    print("❌ No existen sucursales. Inserta sucursales primero.")
    exit()

print(f"✔ Productos encontrados: {len(productos)}")
print(f"✔ Sucursales encontradas: {len(sucursales)}")

# =============================
# 2. Generar 60 registros Recibe
# =============================

def fecha_aleatoria():
    """Genera fechas dentro de los últimos 2 años."""
    dias = random.randint(0, 730)  # 2 años
    return datetime.now() - timedelta(days=dias)

registros = []

for _ in range(60):
    prod = random.choice(productos)
    suc = random.choice(sucursales)

    registros.append({
        "id_producto": prod["_id"],
        "id_sucursal": suc["_id"],
        "fecha": fecha_aleatoria(),
        "cantidad": random.randint(1, 500)  # Cantidad recibida
    })

# =============================
# 3. Insertar en la colección
# =============================

resultado = db.recibe.insert_many(registros)
print(f"✔ Se insertaron {len(resultado.inserted_ids)} registros en 'recibe'.")
