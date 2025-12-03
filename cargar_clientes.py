from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student"
Database_name = "homecenter"

client = MongoClient(uri)
db = client[Database_name]

clientes = [
    {"nombre": "Juan", "apellido": "Pérez", "correo": "juan.perez@email.com", "direccion": "Calle 10 #12-34", "telefono": "3001234567"},
    {"nombre": "María", "apellido": "Gómez", "correo": "maria.gomez@email.com", "direccion": "Carrera 5 #45-21", "telefono": "3012345678"},
    {"nombre": "Carlos", "apellido": "Rodríguez", "correo": "carlos.rodriguez@email.com", "direccion": "Av. Siempre Viva 742", "telefono": "3023456789"},
    {"nombre": "Luisa", "apellido": "Fernández", "correo": "luisa.fernandez@email.com", "direccion": "Calle 8 #9-10", "telefono": "3034567890"},
    {"nombre": "Andrés", "apellido": "Martínez", "correo": "andres.martinez@email.com", "direccion": "Carrera 14 #22-33", "telefono": "3045678901"},
    {"nombre": "Sofía", "apellido": "Ramírez", "correo": "sofia.ramirez@email.com", "direccion": "Calle 7 #15-18", "telefono": "3056789012"},
    {"nombre": "Jorge", "apellido": "López", "correo": "jorge.lopez@email.com", "direccion": "Calle 20 #4-55", "telefono": "3067890123"},
    {"nombre": "Camila", "apellido": "Torres", "correo": "camila.torres@email.com", "direccion": "Av. Libertador 56-78", "telefono": "3078901234"},
    {"nombre": "Mateo", "apellido": "Hernández", "correo": "mateo.hernandez@email.com", "direccion": "Carrera 9 #88-22", "telefono": "3089012345"},
    {"nombre": "Valentina", "apellido": "Díaz", "correo": "valentina.diaz@email.com", "direccion": "Calle 50 #11-60", "telefono": "3090123456"},
    {"nombre": "Sebastián", "apellido": "Jiménez", "correo": "sebastian.jimenez@email.com", "direccion": "Calle 15 #40-20", "telefono": "3101234567"},
    {"nombre": "Daniela", "apellido": "Ruiz", "correo": "daniela.ruiz@email.com", "direccion": "Carrera 33 #9-80", "telefono": "3112345678"},
    {"nombre": "Felipe", "apellido": "Moreno", "correo": "felipe.moreno@email.com", "direccion": "Calle 21 #3-44", "telefono": "3123456789"},
    {"nombre": "Paula", "apellido": "Castaño", "correo": "paula.castano@email.com", "direccion": "Carrera 50 #60-70", "telefono": "3134567890"},
    {"nombre": "Ricardo", "apellido": "Vargas", "correo": "ricardo.vargas@email.com", "direccion": "Av. del Río 12-90", "telefono": "3145678901"},
    {"nombre": "Natalia", "apellido": "Suárez", "correo": "natalia.suarez@email.com", "direccion": "Calle 44 #7-15", "telefono": "3156789012"},
    {"nombre": "Tomás", "apellido": "Cortés", "correo": "tomas.cortes@email.com", "direccion": "Carrera 12 #45-30", "telefono": "3167890123"},
    {"nombre": "Gabriela", "apellido": "Mejía", "correo": "gabriela.mejia@email.com", "direccion": "Calle 66 #13-44", "telefono": "3178901234"},
    {"nombre": "Diego", "apellido": "García", "correo": "diego.garcia@email.com", "direccion": "Carrera 8 #77-88", "telefono": "3189012345"},
    {"nombre": "Laura", "apellido": "Salazar", "correo": "laura.salazar@email.com", "direccion": "Av. Central 23-45", "telefono": "3190123456"},
    {"nombre": "Pedro", "apellido": "Mendoza", "correo": "pedro.mendoza@email.com", "direccion": "Calle 34 #8-20", "telefono": "3201234567"},
    {"nombre": "Claudia", "apellido": "Rojas", "correo": "claudia.rojas@email.com", "direccion": "Carrera 22 #5-67", "telefono": "3212345678"},
    {"nombre": "Manuel", "apellido": "Ortiz", "correo": "manuel.ortiz@email.com", "direccion": "Calle 11 #23-45", "telefono": "3223456789"},
    {"nombre": "Elena", "apellido": "Muñoz", "correo": "elena.munoz@email.com", "direccion": "Carrera 17 #14-25", "telefono": "3234567890"},
    {"nombre": "David", "apellido": "Navarro", "correo": "david.navarro@email.com", "direccion": "Calle 6 #9-11", "telefono": "3245678901"},
    {"nombre": "Diana", "apellido": "Cano", "correo": "diana.cano@email.com", "direccion": "Carrera 44 #22-10", "telefono": "3256789012"},
    {"nombre": "Santiago", "apellido": "Gil", "correo": "santiago.gil@email.com", "direccion": "Calle 18 #34-56", "telefono": "3267890123"},
    {"nombre": "Isabela", "apellido": "Reyes", "correo": "isabela.reyes@email.com", "direccion": "Carrera 9 #10-11", "telefono": "3278901234"},
    {"nombre": "Oscar", "apellido": "Morales", "correo": "oscar.morales@email.com", "direccion": "Calle 60 #12-22", "telefono": "3289012345"},
    {"nombre": "Lina", "apellido": "Peña", "correo": "lina.pena@email.com", "direccion": "Carrera 3 #8-19", "telefono": "3290123456"},
    {"nombre": "Héctor", "apellido": "Vélez", "correo": "hector.velez@email.com", "direccion": "Calle 99 #45-20", "telefono": "3301234567"},
    {"nombre": "Patricia", "apellido": "Castillo", "correo": "patricia.castillo@email.com", "direccion": "Carrera 66 #20-33", "telefono": "3312345678"},
    {"nombre": "Esteban", "apellido": "Cuellar", "correo": "esteban.cuellar@email.com", "direccion": "Calle 13 #33-90", "telefono": "3323456789"},
    {"nombre": "Juliana", "apellido": "Acosta", "correo": "juliana.acosta@email.com", "direccion": "Carrera 40 #4-56", "telefono": "3334567890"},
    {"nombre": "Mauricio", "apellido": "Núñez", "correo": "mauricio.nunez@email.com", "direccion": "Calle 4 #11-12", "telefono": "3345678901"},
    {"nombre": "Verónica", "apellido": "Espinosa", "correo": "veronica.espinosa@email.com", "direccion": "Carrera 27 #7-89", "telefono": "3356789012"},
    {"nombre": "Hernán", "apellido": "Cardona", "correo": "hernan.cardona@email.com", "direccion": "Calle 55 #6-70", "telefono": "3367890123"},
    {"nombre": "Mónica", "apellido": "Cifuentes", "correo": "monica.cifuentes@email.com", "direccion": "Carrera 31 #50-22", "telefono": "3378901234"},
    {"nombre": "Cristian", "apellido": "Valencia", "correo": "cristian.valencia@email.com", "direccion": "Calle 40 #19-33", "telefono": "3389012345"},
    {"nombre": "Sara", "apellido": "Guerrero", "correo": "sara.guerrero@email.com", "direccion": "Carrera 28 #88-20", "telefono": "3390123456"},
    {"nombre": "Álvaro", "apellido": "Perdomo", "correo": "alvaro.perdomo@email.com", "direccion": "Calle 32 #9-90", "telefono": "3401234567"},
    {"nombre": "Melissa", "apellido": "Pardo", "correo": "melissa.pardo@email.com", "direccion": "Carrera 21 #3-78", "telefono": "3412345678"},
    {"nombre": "Fernando", "apellido": "Rivera", "correo": "fernando.rivera@email.com", "direccion": "Calle 16 #17-55", "telefono": "3423456789"},
    {"nombre": "Adriana", "apellido": "Ospina", "correo": "adriana.ospina@email.com", "direccion": "Carrera 11 #9-10", "telefono": "3434567890"},
    {"nombre": "Simón", "apellido": "León", "correo": "simon.leon@email.com", "direccion": "Calle 14 #20-66", "telefono": "3445678901"},
    {"nombre": "Patricio", "apellido": "Arango", "correo": "patricio.arango@email.com", "direccion": "Carrera 36 #40-23", "telefono": "3456789012"},
    {"nombre": "Nicole", "apellido": "Montoya", "correo": "nicole.montoya@email.com", "direccion": "Calle 10 #8-50", "telefono": "3467890123"},
    {"nombre": "Germán", "apellido": "Pineda", "correo": "german.pineda@email.com", "direccion": "Carrera 80 #9-60", "telefono": "3478901234"},
    {"nombre": "Liliana", "apellido": "Restrepo", "correo": "liliana.restrepo@email.com", "direccion": "Calle 22 #3-77", "telefono": "3489012345"},
    {"nombre": "Pablo", "apellido": "Zapata", "correo": "pablo.zapata@email.com", "direccion": "Carrera 15 #90-10", "telefono": "3490123456"}
]

db.cliente.insert_many(clientes)
print("✔ 50 clientes insertados correctamente.")

