from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

# Lista de registros
data = [
    {
        "nombre_sucursal": "Homecenter Norte",
        "direccion": "Av. Caracas # 123-45",
        "ciudad": "Bogotá",
        "telefono": "6014458000",
        "capacidad_parqueadero": 120,
        "descripcion": "Sucursal amplia con alta demanda.",
        "vehiculos": [
            {"placa": "ABC123", "estado": "Disponible"},
            {"placa": "XYZ987", "estado": "En mantenimiento"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Sur",
        "direccion": "Calle 80 Sur # 10-22",
        "ciudad": "Bogotá",
        "telefono": "6018804321",
        "capacidad_parqueadero": 90,
        "descripcion": "Sucursal con horario extendido.",
        "vehiculos": [
            {"placa": "DFG456", "estado": "Disponible"},
            {"placa": "GHJ321", "estado": "Reservado"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Medellín Centro",
        "direccion": "Cra 50 # 51-28",
        "ciudad": "Medellín",
        "telefono": "6042359988",
        "capacidad_parqueadero": 140,
        "descripcion": "Sucursal céntrica con alto tráfico.",
        "vehiculos": [
            {"placa": "MDL123", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Medellín Poblado",
        "direccion": "Calle 10 # 43-50",
        "ciudad": "Medellín",
        "telefono": "6047652233",
        "capacidad_parqueadero": 180,
        "descripcion": "Sucursal Premium en el Poblado.",
        "vehiculos": [
            {"placa": "POB890", "estado": "En mantenimiento"},
            {"placa": "POB567", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Cali Norte",
        "direccion": "Av. 6 Norte # 34-55",
        "ciudad": "Cali",
        "telefono": "6023456777",
        "capacidad_parqueadero": 200,
        "descripcion": "Sucursal con zona de construcciones.",
        "vehiculos": [
            {"placa": "CAL001", "estado": "Disponible"},
            {"placa": "CAL987", "estado": "Reservado"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Cali Sur",
        "direccion": "Cra 56 # 12-90",
        "ciudad": "Cali",
        "telefono": "6029988776",
        "capacidad_parqueadero": 150,
        "descripcion": "Sucursal orientada a remodelación.",
        "vehiculos": [
            {"placa": "CSUR321", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Barranquilla Norte",
        "direccion": "Calle 84 # 51B-23",
        "ciudad": "Barranquilla",
        "telefono": "6053345566",
        "capacidad_parqueadero": 130,
        "descripcion": "Sucursal moderna con amplio acopio.",
        "vehiculos": [
            {"placa": "BAR123", "estado": "Disponible"},
            {"placa": "BAR543", "estado": "En mantenimiento"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Barranquilla Sur",
        "direccion": "Cra 43 # 76-90",
        "ciudad": "Barranquilla",
        "telefono": "6056678899",
        "capacidad_parqueadero": 110,
        "descripcion": "Sucursal de menor tamaño.",
        "vehiculos": [
            {"placa": "BSUR678", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Bucaramanga Cabecera",
        "direccion": "Calle 36 # 45-10",
        "ciudad": "Bucaramanga",
        "telefono": "6076123344",
        "capacidad_parqueadero": 95,
        "descripcion": "Sucursal ubicada en zona residencial.",
        "vehiculos": [
            {"placa": "BUC777", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Bucaramanga Real",
        "direccion": "Cra 27 # 15-20",
        "ciudad": "Bucaramanga",
        "telefono": "6077445511",
        "capacidad_parqueadero": 160,
        "descripcion": "Sucursal con gran inventario.",
        "vehiculos": [
            {"placa": "BUC111", "estado": "Reservado"},
            {"placa": "BUC222", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Cartagena Centro",
        "direccion": "Av. Venezuela # 10-30",
        "ciudad": "Cartagena",
        "telefono": "6056688900",
        "capacidad_parqueadero": 140,
        "descripcion": "Sucursal cerca del centro histórico.",
        "vehiculos": [
            {"placa": "CTG123", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Cartagena Bocagrande",
        "direccion": "Cra 1 # 7-20",
        "ciudad": "Cartagena",
        "telefono": "6052284455",
        "capacidad_parqueadero": 100,
        "descripcion": "Sucursal exclusiva en zona turística.",
        "vehiculos": [
            {"placa": "CTG999", "estado": "En mantenimiento"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Manizales Centro",
        "direccion": "Calle 23 # 22-19",
        "ciudad": "Manizales",
        "telefono": "6067741233",
        "capacidad_parqueadero": 80,
        "descripcion": "Sucursal de tamaño medio.",
        "vehiculos": [
            {"placa": "MNZ123", "estado": "Disponible"},
            {"placa": "MNZ456", "estado": "Reservado"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Manizales Fundadores",
        "direccion": "Cra 21 # 34-51",
        "ciudad": "Manizales",
        "telefono": "6065217890",
        "capacidad_parqueadero": 110,
        "descripcion": "Sucursal con gran sección de pintura.",
        "vehiculos": [
            {"placa": "MNZ890", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Pereira Centro",
        "direccion": "Cra 8 # 20-44",
        "ciudad": "Pereira",
        "telefono": "6063345567",
        "capacidad_parqueadero": 105,
        "descripcion": "Sucursal céntrica con flujo constante.",
        "vehiculos": [
            {"placa": "PRR111", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Pereira Circunvalar",
        "direccion": "Av. Circunvalar # 15-77",
        "ciudad": "Pereira",
        "telefono": "6067562233",
        "capacidad_parqueadero": 150,
        "descripcion": "Sucursal moderna recientemente renovada.",
        "vehiculos": [
            {"placa": "PRR222", "estado": "Reservado"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Pasto Centro",
        "direccion": "Calle 18 # 22-11",
        "ciudad": "Pasto",
        "telefono": "6027319990",
        "capacidad_parqueadero": 70,
        "descripcion": "Sucursal con secciones compactas.",
        "vehiculos": [
            {"placa": "PST123", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Pasto Sur",
        "direccion": "Cra 12 # 5-66",
        "ciudad": "Pasto",
        "telefono": "6022234556",
        "capacidad_parqueadero": 90,
        "descripcion": "Sucursal enfocada en ferretería.",
        "vehiculos": [
            {"placa": "PST678", "estado": "En mantenimiento"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Villavicencio Centro",
        "direccion": "Calle 15 # 33-44",
        "ciudad": "Villavicencio",
        "telefono": "6086691122",
        "capacidad_parqueadero": 130,
        "descripcion": "Sucursal con amplia bodega.",
        "vehiculos": [
            {"placa": "VLL123", "estado": "Disponible"},
            {"placa": "VLL987", "estado": "Reservado"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Villavicencio Norte",
        "direccion": "Cra 40 # 18-33",
        "ciudad": "Villavicencio",
        "telefono": "6088876521",
        "capacidad_parqueadero": 160,
        "descripcion": "Sucursal en zona de expansión urbana.",
        "vehiculos": [
            {"placa": "VLL555", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Montería Centro",
        "direccion": "Calle 35 # 4-21",
        "ciudad": "Montería",
        "telefono": "6047892211",
        "capacidad_parqueadero": 75,
        "descripcion": "Sucursal con gran sección de maderas.",
        "vehiculos": [
            {"placa": "MTR111", "estado": "En mantenimiento"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Montería Norte",
        "direccion": "Cra 6 # 44-90",
        "ciudad": "Montería",
        "telefono": "6048872211",
        "capacidad_parqueadero": 95,
        "descripcion": "Sucursal con alta rotación de inventario.",
        "vehiculos": [
            {"placa": "MTR222", "estado": "Disponible"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Ibagué Centro",
        "direccion": "Cra 4 # 12-55",
        "ciudad": "Ibagué",
        "telefono": "6082215543",
        "capacidad_parqueadero": 85,
        "descripcion": "Sucursal histórica con buena atención.",
        "vehiculos": [
            {"placa": "IBG123", "estado": "Disponible"},
            {"placa": "IBG321", "estado": "Reservado"}
        ]
    },
    {
        "nombre_sucursal": "Homecenter Ibagué Jardín",
        "direccion": "Calle 60 # 7-20",
        "ciudad": "Ibagué",
        "telefono": "6087789900",
        "capacidad_parqueadero": 110,
        "descripcion": "Sucursal rodeada de zonas comerciales.",
        "vehiculos": [
            {"placa": "IBG789", "estado": "Disponible"}
        ]
    }
]

# Inserción masiva
result = db.sucursal.insert_many(data)
print("Registros insertados:", len(result.inserted_ids))
