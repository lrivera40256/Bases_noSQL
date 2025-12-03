from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@student.gdj28nn.mongodb.net/?appName=student")
db = client["homecenter"]

productos = [
    {
        "nombre_producto": "Router Recortador Eléctrico 650W",
        "descripcion": "Herramienta recortadora de madera compacta y precisa.",
        "descripcion_larga": "Router recortador de 650W ideal para acabados, biselados y detalles en madera. Cuenta con base transparente para mayor visibilidad, control de profundidad y diseño ergonómico para uso prolongado.",
        "precio": 249900,
        "marca": "DeWalt",
        "categoria": {
            "nombre_categoria_producto": "Herramientas Eléctricas",
            "descripcion": "Herramientas para corte, fresado y acabados en madera."
        },
        "proveedor": {
            "nombre_proveedor": "ProveTools S.A.S.",
            "telefono": "3102233445",
            "correo": "ventas@provetools.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1h3QXzqDHZDH_b0WzrsqDiOMoGGCNIF_a"
    },
    {
        "nombre_producto": "Combo Sierra Circular + Lijadora Orbital",
        "descripcion": "Kit de sierra circular y lijadora orbital Stanley.",
        "descripcion_larga": "Combo para trabajos de carpintería que incluye sierra circular de 7 1/4 pulgadas con disco de 24 dientes y lijadora orbital de 1/4 hoja. Perfecto para cortes rápidos y acabados suaves en madera.",
        "precio": 389900,
        "marca": "Stanley",
        "categoria": {
            "nombre_categoria_producto": "Herramientas Eléctricas",
            "descripcion": "Herramientas para corte y lijado."
        },
        "proveedor": {
            "nombre_proveedor": "Distribuidora Industrial S.A.",
            "telefono": "3124567890",
            "correo": "contacto@dindustrial.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1yIRRjnpYDC8cI3491wG28D63hW-3XNyJ"
    },
    {
        "nombre_producto": "Caladora Inalámbrica 20V con Maletín",
        "descripcion": "Caladora profesional inalámbrica XR.",
        "descripcion_larga": "Caladora inalámbrica 20V XR ideal para cortes curvos y rectos en madera y metal. Incluye batería 5Ah, cargador y maletín rígido para transporte. Ofrece control de velocidad y sistema anti-vibración.",
        "precio": 799900,
        "marca": "DeWalt",
        "categoria": {
            "nombre_categoria_producto": "Herramientas Inalámbricas",
            "descripcion": "Herramientas a batería para carpintería y construcción."
        },
        "proveedor": {
            "nombre_proveedor": "ProveTools S.A.S.",
            "telefono": "3102233445",
            "correo": "ventas@provetools.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1In9mqE4qp_tYh9Uy5JCDGix85XljiBnx"
    },
    {
        "nombre_producto": "Sierra de Mesa DeWalt 60V Max",
        "descripcion": "Sierra de banco inalámbrica de alto rendimiento.",
        "descripcion_larga": "Sierra de mesa 60V con motor brushless, guía de corte ajustable y superficie de aluminio. Ideal para cortes longitudinales y transversales con precisión en obras y talleres.",
        "precio": 1999900,
        "marca": "DeWalt",
        "categoria": {
            "nombre_categoria_producto": "Herramientas de Carpintería",
            "descripcion": "Equipos para corte y dimensionado de madera."
        },
        "proveedor": {
            "nombre_proveedor": "Ferretería Industrial ProServicios",
            "telefono": "3017894455",
            "correo": "ferreteria@proservicios.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1yIRRjnpYDC8cI3491wG28D63hW-3XNyJ"
    },
    {
        "nombre_producto": "Sierra de Banco con Patas + 2 Discos",
        "descripcion": "Sierra de mesa portátil con estructura metálica.",
        "descripcion_larga": "Sierra de banco con motor de 1500W, mesa extensible y guía de corte. Incluye dos discos adicionales kwb. Ideal para proyectos de carpintería en talleres y obras.",
        "precio": 999900,
        "marca": "Skil",
        "categoria": {
            "nombre_categoria_producto": "Herramientas de Carpintería",
            "descripcion": "Herramientas para corte de madera."
        },
        "proveedor": {
            "nombre_proveedor": "Distribuidora Industrial S.A.",
            "telefono": "3124567890",
            "correo": "contacto@dindustrial.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=17eFwaycHcy9rWcvJyl9dA0mSmQZk2yAm"
    },
    {
        "nombre_producto": "Lavamanos con Mueble en Madera Clara",
        "descripcion": "Mueble con lavamanos integrado, estilo moderno.",
        "descripcion_larga": "Lavamanos de superficie amplia con mueble en madera clara de dos puertas. Resistente a la humedad y perfecto para baños modernos y minimalistas.",
        "precio": 539900,
        "marca": "Corona",
        "categoria": {
            "nombre_categoria_producto": "Baños",
            "descripcion": "Muebles y accesorios para baño."
        },
        "proveedor": {
            "nombre_proveedor": "Importaciones Hogar S.A.S.",
            "telefono": "3157778899",
            "correo": "ventas@importhogar.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1wK1qaiBMwoJh9U0Ce6LqIIergqmQEZu2"
    },
    {
        "nombre_producto": "Lavamanos Flotante con Bowl Negro",
        "descripcion": "Mueble colgante para baño con lavamanos tipo bowl.",
        "descripcion_larga": "Mueble flotante en madera y negro mate con lavamanos tipo bowl en cerámica negra. Ideal para baños modernos con estilo industrial.",
        "precio": 699900,
        "marca": "Corona",
        "categoria": {
            "nombre_categoria_producto": "Baños",
            "descripcion": "Muebles flotantes, lavamanos y accesorios."
        },
        "proveedor": {
            "nombre_proveedor": "Importaciones Hogar S.A.S.",
            "telefono": "3157778899",
            "correo": "ventas@importhogar.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1tPbjHgPJ14OmglhDGHJEQbaJScBeaQXh"
    },
    {
        "nombre_producto": "Puerta de Madera Roble Claro",
        "descripcion": "Puerta interior en acabado madera clara.",
        "descripcion_larga": "Puerta en madera tipo roble claro con manija metálica negra. Ideal para habitaciones o zonas interiores con diseño moderno y cálido.",
        "precio": 499900,
        "marca": "Madecentro",
        "categoria": {
            "nombre_categoria_producto": "Carpintería y Maderas",
            "descripcion": "Puertas, marcos y accesorios de madera."
        },
        "proveedor": {
            "nombre_proveedor": "Maderas del Valle",
            "telefono": "3147894562",
            "correo": "contacto@mvalle.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1iaKnYIy7jPUARjPaAll3INmZ8BTv21L6"
    },
    {
        "nombre_producto": "Lavadora Automática 18kg Negra",
        "descripcion": "Lavadora de carga superior en color negro premium.",
        "descripcion_larga": "Lavadora de 18kg con apertura superior, múltiples ciclos de lavado, nivel automático de agua y panel digital. Ideal para familias grandes.",
        "precio": 1699900,
        "marca": "Haceb",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Lavadoras, secadoras y equipos para el hogar."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroDistribuciones S.A.",
            "telefono": "3124567890",
            "correo": "contacto@electrodistribuciones.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1yRc8_r6WtL7_1AwDeeaTk2YJrWx2MXHE"
    },
    {
        "nombre_producto": "Lavadora Automática 18kg Negra (Vista en Perspectiva)",
        "descripcion": "Lavadora vista lateral para referencia de diseño.",
        "descripcion_larga": "Lavadora de carga superior con diseño moderno en color negro, panel digital, tapa amplia y sistema eficiente de lavado. Modelo ideal para uso familiar.",
        "precio": 1699900,
        "marca": "Haceb",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Lavadoras y equipos de lavado."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroDistribuciones S.A.",
            "telefono": "3124567890",
            "correo": "contacto@electrodistribuciones.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1UvNxepC2hHtKuw6u62EzcE75ybySo4k5"
    }
    {
        "nombre_producto": "Estufa Empotrable 5 Quemadores Vidrio Negro",
        "descripcion": "Cubierta a gas de 5 quemadores con parrillas en hierro fundido.",
        "descripcion_larga": "Cubierta empotrable en vidrio templado negro con 5 quemadores, incluyendo quemador central de alta potencia. Parrillas en hierro fundido, perillas frontales metálicas y encendido eléctrico. Diseño moderno para cocinas integrales.",
        "precio": 1199900,
        "marca": "Indurama",
        "categoria": { "nombre_categoria_producto": "Cocinas y Empotrables", "descripcion": "Cubiertas, hornos y campanas." },
        "proveedor": { "nombre_proveedor": "ElectroDistribuciones S.A.", "telefono": "3124567890", "correo": "contacto@electrodistribuciones.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1wAFA2CYpQMIU_P-np9MttsyGIDl1YJJd	"
    },
    # 12) Parrilla mixta gas + carbón (Mr.Beef)
    {
        "nombre_producto": "Parrilla Doble Gas y Carbón con Quemador Lateral",
        "descripcion": "Barbacoa con dos cámaras independientes y ruedas de transporte.",
        "descripcion_larga": "Parrillera mixta con cámara a gas y cámara a carbón, termómetros en tapa, 3 perillas de control, quemador lateral auxiliar y repisa inferior. Chasis metálico con ruedas para fácil movilidad, ideal para asados al aire libre.",
        "precio": 1699900,
        "marca": "Mr.Beef",
        "categoria": { "nombre_categoria_producto": "Parrillas y Asadores", "descripcion": "Parrillas a gas, carbón y eléctricas." },
        "proveedor": { "nombre_proveedor": "Outdoor Supply S.A.S.", "telefono": "3207788899", "correo": "ventas@outdoorsupply.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1Kxtv3ql_8VsS_3-1J5B59OGqwfxR44tM"
    },
    # 13) Sofá/camastro exterior madera + cojines grises
    {
        "nombre_producto": "Sofá Camastro Exterior en Madera con Cojines Grises",
        "descripcion": "Sofá convertible con estructura en madera natural.",
        "descripcion_larga": "Mueble para terraza con estructura en madera y cojines grises de alta densidad. Patas plegables y laterales con función de reclinado para usar como camastro. Ideal para balcones y jardines.",
        "precio": 899900,
        "marca": "Home Collection",
        "categoria": { "nombre_categoria_producto": "Muebles de Exterior", "descripcion": "Sofás, camastros y poltronas para terraza." },
        "proveedor": { "nombre_proveedor": "Verde & Madera S.A.S.", "telefono": "3114567788", "correo": "contacto@verdemadera.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=13j6fzGtDnoZ16Z6LP3w4DXJwdmjoEjgP"
    },
    # 14) Comedor exterior ratán 6 puestos con vidrio
    {
        "nombre_producto": "Comedor Exterior 6 Puestos Ratán Sintético",
        "descripcion": "Mesa con cubierta en vidrio templado y 6 sillas con brazos.",
        "descripcion_larga": "Set para terraza con estructura metálica y recubrimiento en ratán sintético color beige. Mesa rectangular con vidrio templado y seis sillas ergonómicas con apoyabrazos. Resistente a intemperie.",
        "precio": 1599900,
        "marca": "Home Collection",
        "categoria": { "nombre_categoriaproducto": "Muebles de Exterior", "descripcion": "Comedores de jardín y terrazas." },
        "proveedor": { "nombre_proveedor": "Verde & Madera S.A.S.", "telefono": "3114567788", "correo": "contacto@verdemadera.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1MMfu_3fnNIAUvQY9yka1LW6OZ85cWls-"
    },
    # 15) Comedor exterior 4 puestos con sombrilla
    {
        "nombre_producto": "Comedor Exterior 4 Puestos con Sombrilla",
        "descripcion": "Mesa de vidrio con sillas plegables y parasol central.",
        "descripcion_larga": "Conjunto para jardín con mesa cuadrada de vidrio templado, cuatro sillas plegables en textilene marrón y sombrilla del mismo tono con mástil central. Estructura metálica resistente a exteriores.",
        "precio": 799900,
        "marca": "Outdoor Basic",
        "categoria": { "nombre_categoria_producto": "Muebles de Exterior", "descripcion": "Conjuntos con sombrilla para jardín." },
        "proveedor": { "nombre_proveedor": "Outdoor Supply S.A.S.", "telefono": "3207788899", "correo": "ventas@outdoorsupply.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1tY0NzI5wPlcAf5fEWcCiK5rKJYTCvJrO"
    },
    # 16) Sala exterior madera + cuerdas + cojines beige
    {
        "nombre_producto": "Sala Exterior Madera y Cuerdas con Mesa",
        "descripcion": "Sofá 3 puestos + 2 poltronas + mesa de centro.",
        "descripcion_larga": "Set de sala para terraza con estructura en madera clara y laterales en cuerda tejida. Cojinería color beige de alta densidad y mesa de centro a juego. Estilo natural y moderno.",
        "precio": 2999900,
        "marca": "Home Collection",
        "categoria": { "nombre_categoria_producto": "Muebles de Exterior", "descripcion": "Salas de exterior completas." },
        "proveedor": { "nombre_proveedor": "Verde & Madera S.A.S.", "telefono": "3114567788", "correo": "contacto@verdemadera.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=142MWGaIDk9qN5MxMbUg2m6IhCY-ajr9d"
    },
    # 17) Sala exterior metal + ratán oscuro
    {
        "nombre_producto": "Sala Exterior Ratán Sintético Gris Oscuro",
        "descripcion": "Loveseat, 2 poltronas y mesa de centro.",
        "descripcion_larga": "Conjunto con estructura metálica negra, paneles en ratán sintético gris y cojines color arena. Mesa de centro con superficie tipo madera. Acabados resistentes para uso prolongado en exterior.",
        "precio": 1899900,
        "marca": "Urban Garden",
        "categoria": { "nombre_categoria_producto": "Muebles de Exterior", "descripcion": "Salas y conjuntos modulares." },
        "proveedor": { "nombre_proveedor": "Outdoor Supply S.A.S.", "telefono": "3207788899", "correo": "ventas@outdoorsupply.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1M1V9wWrL52s7zs50YJVNbeFqJl0E5kK_"
    },
    # 18) Sala exterior ratán beige cúbica
    {
        "nombre_producto": "Sala Exterior Ratán Beige 4 Piezas",
        "descripcion": "Sofá 3 puestos, 2 poltronas y mesa con vidrio.",
        "descripcion_larga": "Set con diseño cúbico en ratán sintético beige, cojinería blanca y mesa de centro con cubierta de vidrio. Estilo minimalista y robusto para zonas sociales al aire libre.",
        "precio": 2799900,
        "marca": "Home Collection",
        "categoria": { "nombre_categoria_producto": "Muebles de Exterior", "descripcion": "Conjuntos de terraza premium." },
        "proveedor": { "nombre_proveedor": "Verde & Madera S.A.S.", "telefono": "3114567788", "correo": "contacto@verdemadera.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1aW8f1qnNYKzf3Bi1OrwTlF0uRD72QPpM"
    },
    # 19) Congelador horizontal pequeño (Challenger)
    {
        "nombre_producto": "Congelador Horizontal 100 L Blanco",
        "descripcion": "Freezer compacto con control frontal de temperatura.",
        "descripcion_larga": "Congelador horizontal de 100 litros, tapa abatible, indicador luminoso de funcionamiento y sistema de drenaje. Ideal para almacenar alimentos congelados en casa o negocio pequeño.",
        "precio": 899900,
        "marca": "Challenger",
        "categoria": { "nombre_categoria_producto": "Electrodomésticos", "descripcion": "Refrigeración y congelación." },
        "proveedor": { "nombre_proveedor": "ElectroDistribuciones S.A.", "telefono": "3124567890", "correo": "contacto@electrodistribuciones.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1G9wgBNE-SLfpNFQKh-vDxT_nc40xF0NJ"
    },
    # 20) Congelador/Refrigerador vertical (Challenger)
]