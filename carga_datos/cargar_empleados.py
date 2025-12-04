from pymongo import MongoClient
from bson import ObjectId
import random

uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

areas = list(db.area.find({}, {"_id": 1, "nombre_area": 1}))

if not areas:
    print("❌ No existen áreas. Inserta áreas primero.")
    exit()

print(f"✔ Áreas encontradas: {len(areas)}")

nombres = [
    "Carlos", "Ana", "Luis", "María", "Jorge", "Laura", "Andrés", "Valentina", "Sofía",
    "Daniel", "Camila", "Felipe", "Juliana", "Sebastián", "Paula", "Miguel", "Diana",
    "Mateo", "Isabella", "Santiago", "Fernanda", "Brayan", "Adriana", "Kevin", "Lucía",
    "Tomás", "Gabriela", "Simón", "Mariana", "Juan", "Nicole", "Samuel"
]

apellidos = [
    "García", "Martínez", "Rodríguez", "López", "Hernández", "Pérez", "Gómez", "Díaz",
    "Moreno", "Romero", "Vargas", "Silva", "Rojas", "Torres", "Castro", "Ortega",
    "Medina", "Chávez", "Reyes", "Cortés", "Nieto", "Acosta", "Mora", "Suárez"
]

cargos = [
    "Asesor Comercial", "Jefe de Área", "Cajero", "Auxiliar de Inventario",
    "Supervisor de Ventas", "Técnico de Instalación", "Atención al Cliente",
    "Coordinador de Seguridad", "Auxiliar de Bodega", "Vendedor Especializado",
    "Administrador de Área", "Técnico Electricista", "Técnico en Mantenimiento"
]

calles = [
    "Calle 12 #4-", "Carrera 15 #20-", "Calle 8 #30-", "Avenida 19 #45-",
    "Diagonal 23 #7-", "Transversal 9 #55-", "Calle 25 #18-", "Carrera 3 #14-",
]

telefonos_base = ["300", "301", "302", "310", "311", "320", "321", "322"]

empleados = []

for i in range(100):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)

    correo = f"{nombre.lower()}.{apellido.lower()}{i}@homecenter.com"
    cargo = random.choice(cargos)
    direccion = f"{random.choice(calles)}{random.randint(10, 99)}"
    telefono = f"{random.choice(telefonos_base)}{random.randint(1000000, 9999999)}"

    area_random = random.choice(areas)

    empleados.append({
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "cargo": cargo,
        "direccion": direccion,
        "telefono": telefono,
        "id_area": area_random["_id"]
    })

resultado = db.empleado.insert_many(empleados)

print(f"✔ Se insertaron {len(resultado.inserted_ids)} empleados correctamente.")
