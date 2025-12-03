from pymongo import MongoClient
from bson import ObjectId
import random

uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

# 1. Obtener todos los IDs reales de sucursal
sucursales = list(db.sucursal.find({}, {"_id": 1, "nombre_sucursal": 1}))

if not sucursales:
    print("❌ No hay sucursales en la base de datos. Inserta sucursales primero.")
    exit()

print("✔ Sucursales encontradas:")
for s in sucursales:
    print(f"- {s['_id']} | {s.get('nombre_sucursal', '(sin nombre)')}")

# 2. Lista de nombres de áreas
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

# 3. Generar entre 20 y 30 áreas, asignando id_sucursal real aleatorio
cantidad = random.randint(20, 30)

areas = []
for i in range(cantidad):
    nombre = nombres_areas[i % len(nombres_areas)]
    sucursal_random = random.choice(sucursales)  # ID real
    areas.append({
        "nombre_area": nombre,
        "id_sucursal": sucursal_random["_id"]
    })

# 4. Insertar áreas
resultado = db.area.insert_many(areas)

print(f"\n✔ Se insertaron {len(resultado.inserted_ids)} áreas correctamente.")
