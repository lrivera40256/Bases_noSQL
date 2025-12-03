# -*- coding: utf-8 -*-
from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

print("🚨 Eliminando todas las colecciones existentes...")
for col in db.list_collection_names():
    db[col].drop()
print("✔ Base limpia.\n")

# ==========================================
# VALIDADORES RAG-READY
# ==========================================

try:
    # === CLIENTE ===
    db.create_collection("cliente", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nombre", "apellido", "correo"],
            "properties": {
                "nombre": {"bsonType": "string"},
                "apellido": {"bsonType": "string"},
                "direccion": {"bsonType": "string"},
                "telefono": {"bsonType": "string"},
                "correo": {"bsonType": "string"}
            }
        }
    })

    # === SUCURSAL ===
    db.create_collection("sucursal", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nombre_sucursal", "direccion", "ciudad"],
            "properties": {
                "nombre_sucursal": {"bsonType": "string"},
                "direccion": {"bsonType": "string"},
                "ciudad": {"bsonType": "string"},
                "telefono": {"bsonType": "string"},
                "capacidad_parqueadero": {"bsonType": "int"},
                "descripcion": {"bsonType": "string"},
                "vehiculos": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "object",
                        "required": ["placa", "estado"],
                        "properties": {
                            "placa": {"bsonType": "string"},
                            "estado": {"bsonType": "string"}
                        }
                    }
                }
            }
        }
    })

    # === AREA ===
    db.create_collection("area", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nombre_area", "id_sucursal"],
            "properties": {
                "nombre_area": {"bsonType": "string"},
                "id_sucursal": {"bsonType": "objectId"}
            }
        }
    })

    # === EMPLEADO ===
    db.create_collection("empleado", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nombre", "apellido", "correo", "cargo", "id_area"],
            "properties": {
                "nombre": {"bsonType": "string"},
                "apellido": {"bsonType": "string"},
                "direccion": {"bsonType": "string"},
                "telefono": {"bsonType": "string"},
                "correo": {"bsonType": "string"},
                "cargo": {"bsonType": "string"},
                "id_area": {"bsonType": "objectId"},
            }
        }
    })

    # === PRODUCTO (RAG READY) ===
    db.create_collection("producto", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["nombre_producto", "precio", "marca"],
            "properties": {
                "nombre_producto": {"bsonType": "string"},
                "descripcion": {"bsonType": "string"},

                # Campos nuevos IMPORTANTES
                "descripcion_larga": {"bsonType": "string"},
                "imagen_principal": {"bsonType": "string"},

                "precio": {"bsonType": "double"},
                "marca": {"bsonType": "string"},

                "categoria": {
                    "bsonType": "object",
                    "required": ["nombre_categoria_producto"],
                    "properties": {
                        "nombre_categoria_producto": {"bsonType": "string"},
                        "descripcion": {"bsonType": "string"}
                    }
                },

                # Proveedor embebido como lo pidió el profesor
                "proveedor": {
                    "bsonType": "object",
                    "required": ["nombre_proveedor"],
                    "properties": {
                        "nombre_proveedor": {"bsonType": "string"},
                        "telefono": {"bsonType": "string"},
                        "correo": {"bsonType": "string"}
                    }
                }
            }
        }
    })

    # === RECIBE ===
    db.create_collection("recibe", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["id_producto", "id_sucursal", "fecha", "cantidad"],
            "properties": {
                "id_producto": {"bsonType": "objectId"},
                "id_sucursal": {"bsonType": "objectId"},
                "fecha": {"bsonType": "date"},
                "cantidad": {"bsonType": "int"}
            }
        }
    })

    # === COMPRA ===
    db.create_collection("compra", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["id_cliente"],
            "properties": {
                "id_cliente": {"bsonType": "objectId"},
                "id_sucursal": {"bsonType": "objectId"},
                "fecha": {"bsonType": "date"},

                "comentarios_cliente": {"bsonType": "string"},

                "productosxcompra": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "object",
                        "required": ["id_producto"],
                        "properties": {
                            "id_producto": {"bsonType": "objectId"},
                            "cantidad": {"bsonType": "int"},
                            "devolucion": {
                                "bsonType": "object",
                                "properties": {
                                    "motivo": {"bsonType": "string"},
                                    "fecha": {"bsonType": "date"}
                                }
                            },
                            "servicio_instalacion": {
                                "bsonType": "object",
                                "properties": {
                                    "fecha": {"bsonType": "date"},
                                    "estado": {"bsonType": "string"}
                                }
                            },
                            "envio": {
                                "bsonType": "object",
                                "properties": {
                                    "direccion": {"bsonType": "string"},
                                    "fecha_envio": {"bsonType": "date"},
                                    "estado": {"bsonType": "string"}
                                }
                            }
                        }
                    }
                },

                "factura": {
                    "bsonType": "object",
                    "properties": {
                        "fecha": {"bsonType": "date"},
                        "total": {"bsonType": "double"},
                        "metodo_pago": {"bsonType": "string"}
                    }
                }
            }
        }
    })

    db.create_collection("embeddings_imagen", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["producto_id", "imagen_url", "embedding_imagen"],
            "properties": {

                "producto_id": { "bsonType": "objectId" },    # referencia a producto
                "imagen_url": { "bsonType": "string" },

                "embedding_imagen": {
                    "bsonType": "array",
                    "items": { "bsonType": "double" }
                },

                "metadata": { "bsonType": "object" }
            }
        }
    })

    db.create_collection("embeddings_texto", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["origen", "id_origen", "campo", "texto", "embedding_texto"],
            "properties": {

                "origen": { "bsonType": "string" },          # ejemplo: 'producto', 'cliente', 'sucursal'
                "id_origen": { "bsonType": "objectId" },     # referencia al documento original
                "campo": { "bsonType": "string" },           # ejemplo: 'descripcion', 'direccion', 'descripcion_larga'
                "texto": { "bsonType": "string" },

                "embedding_texto": {
                    "bsonType": "array",
                    "items": { "bsonType": "double" }
                },

                "metadata": { "bsonType": "object" }
            }
        }
    })


    print("✔ TODAS LAS COLECCIONES CON VALIDADORES RAG LISTAS.")

except Exception as e:
    print("❌ Error al crear colecciones:", e)

finally:
    client.close()

