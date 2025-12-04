# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta
import random

# === CONEXIÓN A MONGO ===
uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
client = MongoClient(uri)
db = client["homecenter"]

# === Obtener IDs reales de otras colecciones ===
clientes = list(db.cliente.find({}, {"_id": 1}))
sucursales = list(db.sucursal.find({}, {"_id": 1}))
productos = list(db.producto.find({}, {"_id": 1}))

if not clientes or not sucursales or not productos:
    print("❌ Debes tener clientes, sucursales y productos cargados antes de generar compras.")
    exit()

print(f"✔ {len(clientes)} clientes, {len(sucursales)} sucursales y {len(productos)} productos encontrados.\n")

# === Datos base ===
comentarios = [
    "Excelente servicio y entrega puntual.",
    "Producto llegó en perfectas condiciones.",
    "Recomendado, muy buena atención.",
    "Tuve un problema con el envío, pero se resolvió.",
    "Volvería a comprar sin dudarlo.",
    "Entrega más rápida de lo esperado.",
    "El producto no cumplió mis expectativas.",
    "Muy buena calidad por el precio.",
    "Compra sencilla y confiable.",
    "Atención al cliente sobresaliente."
]

metodos_pago = ["Tarjeta de crédito", "Tarjeta débito", "Efectivo", "Transferencia", "PSE"]

estados_envio = ["Entregado", "En camino", "Pendiente"]
direcciones = [
    "Calle 10 #15-23", "Carrera 7 #45-10", "Av. Central 12-34", "Calle 80 #9-20",
    "Carrera 50 #33-11", "Av. Libertador 60-22", "Calle 22 #7-89", "Carrera 9 #40-15"
]

# === Generar 100 compras ===
compras = []
for i in range(100):
    cliente = random.choice(clientes)
    sucursal = random.choice(sucursales)
    fecha_compra = datetime.now() - timedelta(days=random.randint(0, 365))

    # Productos de esta compra (1 a 4 productos)
    items = []
    for _ in range(random.randint(1, 4)):
        producto = random.choice(productos)
        cantidad = random.randint(1, 5)

        item = {
            "id_producto": producto["_id"],
            "cantidad": cantidad,
            "envio": {
                "direccion": random.choice(direcciones),
                "fecha_envio": fecha_compra + timedelta(days=random.randint(1, 5)),
                "estado": random.choice(estados_envio)
            }
        }

        # Ocasionalmente agrega devolución o instalación
        if random.random() < 0.1:  # 10%
            item["devolucion"] = {
                "motivo": "Producto defectuoso",
                "fecha": fecha_compra + timedelta(days=random.randint(2, 10))
            }

        if random.random() < 0.2:  # 20%
            item["servicio_instalacion"] = {
                "fecha": fecha_compra + timedelta(days=random.randint(1, 3)),
                "estado": random.choice(["Completado", "Pendiente"])
            }

        items.append(item)

    # Calcular total (simulado)
    total = round(random.uniform(50000, 2000000), 2)

    compra = {
        "id_cliente": cliente["_id"],
        "id_sucursal": sucursal["_id"],
        "fecha": fecha_compra,
        "comentarios_cliente": random.choice(comentarios),
        "productosxcompra": items,
        "factura": {
            "fecha": fecha_compra,
            "total": total,
            "metodo_pago": random.choice(metodos_pago)
        }
    }

    compras.append(compra)

# === Insertar en Mongo ===
result = db.compra.insert_many(compras)
print(f"✔ Se insertaron {len(result.inserted_ids)} compras correctamente.")
