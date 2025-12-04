from pymongo import MongoClient
from bson import ObjectId
import random

uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

# 1. Obtener todos los IDs de sucursales existentes
sucursales = list(db.sucursal.find({}, {"_id": 1, "nombre_sucursal": 1}))

if not sucursales:
    print("❌ No hay sucursales en la base de datos. Inserta sucursales primero.")
    exit()

print("✔ Sucursales encontradas:")
for s in sucursales:
    print(f"- {s['_id']} | {s.get('nombre_sucursal', '(sin nombre)')}")

# 2. Lista de posibles nombres de áreas
nombres_areas = [
    "Electrodomésticos", "Herramientas", "Construcción", "Jardinería", "Pinturas",
    "Muebles", "Cocina", "Baños", "Iluminación", "Seguridad",
    "Domótica", "Pisos y Revestimientos", "Decoración", "Ferretería",
    "Organización del Hogar", "Puertas y Ventanas", "Techos y Cubiertas",
    "Materiales Pesados", "Fontanería", "Electricidad", "Automotriz",
    "Línea Blanca", "Suministros Industriales", "Servicios Técnicos",
    "Herramientas Eléctricas", "Herramientas Manuales", "Climatización",
    "Hogar Exterior", "Zona BBQ"
]

# 3. Generar 80 nuevas áreas evitando duplicados
areas_nuevas = []
intentos = 0
while len(areas_nuevas) < 80 and intentos < 200:
    intentos += 1
    nombre = random.choice(nombres_areas)
    sucursal_random = random.choice(sucursales)
    id_sucursal = sucursal_random["_id"]

    # Verificar si ya existe el mismo nombre de área en esa sucursal
    existe = db.area.find_one({
        "nombre_area": nombre,
        "id_sucursal": id_sucursal
    })

    if not existe:
        areas_nuevas.append({
            "nombre_area": nombre,
            "id_sucursal": id_sucursal
        })

# 4. Insertar solo las áreas que no existían
if areas_nuevas:
    resultado = db.area.insert_many(areas_nuevas)
    print(f"\n✔ Se insertaron {len(resultado.inserted_ids)} áreas nuevas correctamente.")
else:
    print("\n⚠ No se insertaron nuevas áreas porque ya existen todas las combinaciones posibles.")
