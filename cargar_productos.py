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
    {
        "nombre_producto": "Nevera Vertical 235 Lts Inoxidable",
        "descripcion": "Refrigerador compacto con puerta reversible y congelador superior.",
        "descripcion_larga": "Nevera vertical de 235 litros marca Challenger con diseño en acero inoxidable, bandejas ajustables y bajo consumo energético. Ideal para espacios pequeños u oficinas.",
        "precio": 1299900,
        "marca": "Challenger",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Refrigeración y conservación de alimentos."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroDistribuciones S.A.",
            "telefono": "3124567890",
            "correo": "contacto@electrodistribuciones.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1NMvvAy-UYlGKDAB1HvYey_A0PPePuGHN"
    },
    {
        "nombre_producto": "Congelador Horizontal 400 L Blanco",
        "descripcion": "Freezer industrial de gran capacidad con control frontal de temperatura.",
        "descripcion_larga": "Congelador horizontal de 400 litros con sistema de drenaje, ruedas para fácil desplazamiento y tapa abatible. Perfecto para uso comercial o doméstico intensivo.",
        "precio": 1899900,
        "marca": "Indufrial",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Congeladores y refrigeradores horizontales."
        },
        "proveedor": {
            "nombre_proveedor": "FrioSolutions Ltda.",
            "telefono": "3109876543",
            "correo": "ventas@friosolutions.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1KgGaBkt4ohMsi1IWJiWq1h9qiqVZeJcM"
    },
    {
        "nombre_producto": "Lavavajillas Empotrable 12 Puestos Acero Inoxidable",
        "descripcion": "Lavavajillas automático de acero inoxidable con dos bandejas y controles digitales.",
        "descripcion_larga": "Lavavajillas empotrable de 12 puestos con sensores de carga, modo ecológico y motor silencioso. Fabricado por Samsung para un lavado eficiente y moderno.",
        "precio": 2699900,
        "marca": "Samsung",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Limpieza automática de utensilios de cocina."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroDistribuciones S.A.",
            "telefono": "3124567890",
            "correo": "contacto@electrodistribuciones.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1TPc3OZeGpoZyz0hzoypt3FKt_6CalY-K"
    },
    {
        "nombre_producto": "Silla Oficina Ergonómica Respaldo Malla Negra",
        "descripcion": "Silla giratoria de oficina con soporte lumbar y ajuste de altura.",
        "descripcion_larga": "Silla ergonómica con base metálica de cinco ruedas, respaldo en malla transpirable y sistema hidráulico de elevación. Ideal para jornadas largas de trabajo.",
        "precio": 349900,
        "marca": "HomeOffice",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Oficina",
            "descripcion": "Sillas, escritorios y mobiliario ergonómico."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1MA6PbeqYm7F-NR_QWiVPymoIomumk_Ne"
    },
    {
        "nombre_producto": "Silla Gamer Recline Pro Blanco y Negro",
        "descripcion": "Silla gamer reclinable con cojines ergonómicos y reposapiés extensible.",
        "descripcion_larga": "Silla gamer de diseño deportivo en cuero sintético bicolor, soporte de cuello y espalda, estructura de acero y ruedas silenciosas. Reclinable hasta 170 grados.",
        "precio": 699900,
        "marca": "Cougar",
        "categoria": {
            "nombre_categoria_producto": "Muebles",
            "descripcion": "Sillas de juego y descanso ergonómicas."
        },
        "proveedor": {
            "nombre_proveedor": "GamerStore S.A.S.",
            "telefono": "3161234567",
            "correo": "ventas@gamerstore.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1BdFi3Q_KvMNg5Wqi_FWC8LXHYRR5XBXt"
    },
    {
        "nombre_producto": "Silla Ejecutiva Alta con Cabecero Gris",
        "descripcion": "Silla ejecutiva de diseño moderno con soporte cervical y base cromada.",
        "descripcion_larga": "Silla ejecutiva con estructura en acero, malla respirable, reposacabezas y apoyabrazos ajustables. Ideal para oficinas modernas o espacios ejecutivos.",
        "precio": 599900,
        "marca": "HomeOffice",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Oficina",
            "descripcion": "Sillas y mobiliario profesional de oficina."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=17976CvaZI552-a3aXwErPq2NK12OBWl3"
    },
    {
        "nombre_producto": "Silla Ejecutiva Blanca con Cabecero",
        "descripcion": "Silla ergonómica con soporte lumbar y diseño elegante en color blanco.",
        "descripcion_larga": "Silla de oficina blanca con respaldo de malla y base metálica cromada. Cuenta con ajuste de altura, soporte de cabeza y ruedas silenciosas.",
        "precio": 629900,
        "marca": "HomeOffice",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Oficina",
            "descripcion": "Mobiliario ergonómico para trabajo prolongado."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1ekCJZLqVfoMDNCRNoa-_QJ4sjxfkNLn8"
    },
    {
        "nombre_producto": "Pintura Viniltex Advanced Mate 5 Galones",
        "descripcion": "Pintura lavable de alta durabilidad para interiores.",
        "descripcion_larga": "Pintura Viniltex Advanced Mate de 5 galones con tecnología antibacteriana, excelente cubrimiento y fácil limpieza. Color blanco para paredes interiores.",
        "precio": 229900,
        "marca": "Pintuco",
        "categoria": {
            "nombre_categoria_producto": "Pinturas",
            "descripcion": "Recubrimientos para paredes interiores y exteriores."
        },
        "proveedor": {
            "nombre_proveedor": "ColorPaint S.A.",
            "telefono": "3187654321",
            "correo": "ventas@colorpaint.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=19lgJalewSYc4ZjgIdUny5KuuvZ2unbdV"
    },
    {
        "nombre_producto": "Pintura TopEx Pro 2000 Blanco 5 Galones",
        "descripcion": "Pintura contratista de alto poder cubriente para interiores.",
        "descripcion_larga": "Pintura TopEx Pro 2000 blanca en presentación de 5 galones, con acabado mate y fácil limpieza. Ideal para proyectos residenciales y comerciales.",
        "precio": 199900,
        "marca": "TopEx",
        "categoria": {
            "nombre_categoria_producto": "Pinturas",
            "descripcion": "Productos de acabado para paredes y techos."
        },
        "proveedor": {
            "nombre_proveedor": "ColorPaint S.A.",
            "telefono": "3187654321",
            "correo": "ventas@colorpaint.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=15qW3f7LpzTxrBtOv3VL89syK63Qu6jJS"
    },
    {
        "nombre_producto": "Pintura Viniltex Advanced Mate 1 Galón",
        "descripcion": "Pintura lavable de acabado mate para interiores.",
        "descripcion_larga": "Pintura Viniltex Advanced Mate de 1 galón con fórmula antibacteriana, color blanco y excelente rendimiento. Ideal para renovar espacios interiores.",
        "precio": 69900,
        "marca": "Pintuco",
        "categoria": {
            "nombre_categoria_producto": "Pinturas",
            "descripcion": "Recubrimientos para uso decorativo interior."
        },
        "proveedor": {
            "nombre_proveedor": "ColorPaint S.A.",
            "telefono": "3187654321",
            "correo": "ventas@colorpaint.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1k1UH37zTrVhV3AOriPt2ZpQX3MvgPy_O"
    },
    {
        "nombre_producto": "Escritorio con Estantería Lateral Roble y Blanco",
        "descripcion": "Escritorio moderno con repisas laterales integradas para almacenamiento.",
        "descripcion_larga": "Escritorio fabricado en madera aglomerada con acabado en roble claro y superficie blanca. Incluye tres repisas laterales ideales para libros, documentos o decoración. Diseño funcional y compacto para espacios de estudio u oficina.",
        "precio": 449900,
        "marca": "RTA Design",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Oficina",
            "descripcion": "Escritorios, estanterías y mobiliario funcional para el hogar y oficina."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=116rJQHHvJ3bDTK-krat4_XE51-aJoCAx"
    },
    {
        "nombre_producto": "Escritorio en L con Estantería Lateral Negro y Roble",
        "descripcion": "Escritorio en L con compartimientos y puerta lateral.",
        "descripcion_larga": "Escritorio multifuncional en forma de L fabricado en melamina color negro y roble claro. Cuenta con compartimientos laterales, una puerta abatible y amplio espacio para computador o estudio.",
        "precio": 549900,
        "marca": "RTA Design",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Oficina",
            "descripcion": "Escritorios, mesas de trabajo y mobiliario funcional."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1XA-925W7Hs1ZwQX5IZ4HGJbK4Dwo7Nwk"
    },
    {
        "nombre_producto": "Escritorio Metálico con Superficie de Vidrio",
        "descripcion": "Escritorio moderno de vidrio templado y estructura metálica.",
        "descripcion_larga": "Escritorio con diseño minimalista de estructura cromada en acero y superficie de vidrio templado. Ideal para espacios modernos, combina durabilidad y elegancia en una sola pieza.",
        "precio": 619900,
        "marca": "UrbanWork",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Oficina",
            "descripcion": "Muebles metálicos modernos y funcionales para oficina."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1313m53WwZavTVe8VIgbOqZ4tC0suIPQZ"
    },
    {
        "nombre_producto": "Centro de Computo Modular Blanco con Biblioteca",
        "descripcion": "Escritorio con torre lateral para CPU y biblioteca incorporada.",
        "descripcion_larga": "Centro de cómputo fabricado en melamina blanca, con espacio para CPU, teclado deslizable y repisas verticales. Incluye biblioteca lateral con tres niveles.",
        "precio": 699900,
        "marca": "RTA Design",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Oficina",
            "descripcion": "Muebles funcionales para equipos de cómputo."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1jtFdGDSFIeiu8b1oRS_QiWUpdCfLrMfn"
    },
    {
        "nombre_producto": "Biblioteca Alta 5 Niveles Color Nogal",
        "descripcion": "Biblioteca vertical de cinco niveles en acabado nogal.",
        "descripcion_larga": "Biblioteca de diseño clásico con cinco niveles amplios para libros, decoraciones o archivos. Fabricada en aglomerado de madera con acabado en color nogal natural.",
        "precio": 369900,
        "marca": "RTA Design",
        "categoria": {
            "nombre_categoria_producto": "Muebles",
            "descripcion": "Estanterías y bibliotecas para el hogar u oficina."
        },
        "proveedor": {
            "nombre_proveedor": "MueblesExpress S.A.S.",
            "telefono": "3145678901",
            "correo": "contacto@mueblesexpress.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1_TGyoMQtiGBF4GHr6n9FSgF-4fe14xC_"
    },
    {
        "nombre_producto": "Organizador Modular 6 Cubos Blanco",
        "descripcion": "Estantería modular con seis compartimientos abiertos.",
        "descripcion_larga": "Estante de seis cubos fabricado en melamina blanca de alta resistencia. Ideal para organización de libros, objetos decorativos o almacenamiento de oficina.",
        "precio": 289900,
        "marca": "HomeStyle",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Hogar",
            "descripcion": "Organizadores y estanterías modulares."
        },
        "proveedor": {
            "nombre_proveedor": "DecoHome S.A.S.",
            "telefono": "3157892345",
            "correo": "info@decohome.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1IjoBnXaPFyU6FOxCQV9wVrGqyJryPW_x"
    },
    {
        "nombre_producto": "Estantería Baja 6 Cubos Blanco Mate",
        "descripcion": "Estantería horizontal moderna para sala o estudio.",
        "descripcion_larga": "Estante de seis compartimientos horizontales con acabado blanco mate. Perfecta para exhibir libros, cajas organizadoras o decoración minimalista.",
        "precio": 319900,
        "marca": "HomeStyle",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Hogar",
            "descripcion": "Estanterías y muebles decorativos modernos."
        },
        "proveedor": {
            "nombre_proveedor": "DecoHome S.A.S.",
            "telefono": "3157892345",
            "correo": "info@decohome.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=168yu5R-f_UziUxAglL19A6uKxmGi-BkP"
    },
    {
        "nombre_producto": "Estantería 8 Cubos con Cajas Textiles Grises",
        "descripcion": "Organizador alto con compartimientos y cajas extraíbles.",
        "descripcion_larga": "Estantería vertical con ocho cubos y cajas de tela gris incluidas. Fabricada en melamina blanca resistente, ideal para espacios de trabajo o dormitorios.",
        "precio": 399900,
        "marca": "HomeStyle",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Hogar",
            "descripcion": "Organizadores con compartimientos y cajones textiles."
        },
        "proveedor": {
            "nombre_proveedor": "DecoHome S.A.S.",
            "telefono": "3157892345",
            "correo": "info@decohome.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1jOM6FwvSy3lbzldrbkUoytpPHiANQM1S"
    },
    {
        "nombre_producto": "Cocina Integral 5 Puertas 1 Cajón Roble y Blanco",
        "descripcion": "Cocina integral compacta con cubierta y lavaplatos incluidos.",
        "descripcion_larga": "Cocina integral de 5 puertas y 1 cajón fabricada en MDP de 15 mm con acabado en roble y blanco. Incluye lavaplatos doble y espacio para estufa o microondas.",
        "precio": 1449900,
        "marca": "RTA Kitchen",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Cocina",
            "descripcion": "Cocinas integrales y modulares listas para instalar."
        },
        "proveedor": {
            "nombre_proveedor": "CocinaFácil S.A.S.",
            "telefono": "3134567890",
            "correo": "ventas@cocinafacil.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1aGYilt9Ix7O0nyKzV2kFiQRfc84OA2i9"
    },
    {
        "nombre_producto": "Cocina Modular en L 7 Puertas Roble y Blanco",
        "descripcion": "Cocina modular con barra lateral y amplio espacio de almacenamiento.",
        "descripcion_larga": "Cocina integral en forma de L con 7 puertas y 2 cajones, superficie de melamina resistente al calor y módulos superiores abiertos. Ideal para hogares modernos.",
        "precio": 2399900,
        "marca": "RTA Kitchen",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Cocina",
            "descripcion": "Módulos de cocina modernos con acabados resistentes."
        },
        "proveedor": {
            "nombre_proveedor": "CocinaFácil S.A.S.",
            "telefono": "3134567890",
            "correo": "ventas@cocinafacil.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1f4otmIwmYQ5vye-y4mitcu4fjOs42OVc"
    },
    {
        "nombre_producto": "Cocina Integral 4 Puertas Madera Natural y Beige",
        "descripcion": "Cocina compacta moderna con acabado natural y beige.",
        "descripcion_larga": "Cocina integral de 4 puertas con superficie de acero inoxidable y estufa empotrada. Acabado en madera natural y beige, diseño elegante y funcional.",
        "precio": 1899900,
        "marca": "RTA Kitchen",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Cocina",
            "descripcion": "Cocinas integrales con superficie metálica y diseño moderno."
        },
        "proveedor": {
            "nombre_proveedor": "CocinaFácil S.A.S.",
            "telefono": "3134567890",
            "correo": "ventas@cocinafacil.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1N5JYjnSum3rbLf2bTgtTxUrGD2bPauY1"
    },
    {
        "nombre_producto": "Cocina Integral Moderna Roble Claro y Negro",
        "descripcion": "Cocina integral compacta con acabados en roble claro y estructura negra.",
        "descripcion_larga": "Cocina integral contemporánea con módulos superiores e inferiores, fabricada en melamina de alta resistencia. Combina tonos de roble natural con estructura negra, aportando un estilo elegante y funcional.",
        "precio": 1899900,
        "marca": "RTA Kitchen",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Cocina",
            "descripcion": "Cocinas integrales modernas con módulos y espacio para electrodomésticos."
        },
        "proveedor": {
            "nombre_proveedor": "CocinaFácil S.A.S.",
            "telefono": "3134567890",
            "correo": "ventas@cocinafacil.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1PRszugOUXtHvHpG6osKaC_poZ4plglKG"
    },
    {
        "nombre_producto": "Cocina en L Moderna Roble Claro y Grafito",
        "descripcion": "Cocina modular en L con amplios compartimientos y diseño elegante.",
        "descripcion_larga": "Cocina integral modular en forma de L, con módulos superiores e inferiores, puertas en tono roble claro y estructura color grafito. Ideal para espacios amplios y modernos.",
        "precio": 2599900,
        "marca": "RTA Kitchen",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Cocina",
            "descripcion": "Cocinas integrales modulares con acabado de madera."
        },
        "proveedor": {
            "nombre_proveedor": "CocinaFácil S.A.S.",
            "telefono": "3134567890",
            "correo": "ventas@cocinafacil.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1K94LZNclNhqHuzgwYRO0XCrUWaE5_Vbu"
    },
    {
        "nombre_producto": "Comedor 6 Puestos Negro con Sillas Acolchadas",
        "descripcion": "Comedor rectangular de 6 puestos con estructura metálica y sillas tapizadas.",
        "descripcion_larga": "Mesa de comedor negra con tablero de vidrio templado y estructura metálica. Incluye seis sillas tapizadas en cuero sintético negro, ofreciendo elegancia y confort en el comedor.",
        "precio": 1299900,
        "marca": "DecoHome",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Comedor",
            "descripcion": "Comedores modernos con estructura metálica y sillas acolchadas."
        },
        "proveedor": {
            "nombre_proveedor": "DecoHome S.A.S.",
            "telefono": "3157892345",
            "correo": "info@decohome.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1uDESXXakDCk_ZCyyAMrGfwteO69OqfXI"
    },
    {
        "nombre_producto": "Comedor 6 Puestos Estilo Escandinavo",
        "descripcion": "Mesa de madera con diseño geométrico y sillas tapizadas en tela.",
        "descripcion_larga": "Comedor de seis puestos con mesa de superficie de madera con patrón geométrico y patas de acero. Incluye seis sillas tapizadas en tonos gris y verde con respaldo curvo para mayor comodidad.",
        "precio": 1549900,
        "marca": "NordicLiving",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Comedor",
            "descripcion": "Comedores de diseño escandinavo con materiales cálidos y modernos."
        },
        "proveedor": {
            "nombre_proveedor": "NordicLiving Ltda.",
            "telefono": "3166549870",
            "correo": "contacto@nordicliving.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1DAs17QpW1iiONXZS3z7Qtzj9qJCgYH9d"
    },
    {
        "nombre_producto": "Comedor 4 Puestos Vidrio y Madera Natural",
        "descripcion": "Mesa cuadrada de vidrio templado con patas de madera y sillas blancas.",
        "descripcion_larga": "Comedor de cuatro puestos con superficie de vidrio templado y patas de madera natural. Incluye cuatro sillas blancas de estilo nórdico, ideal para espacios pequeños y modernos.",
        "precio": 899900,
        "marca": "HomeStyle",
        "categoria": {
            "nombre_categoria_producto": "Muebles de Comedor",
            "descripcion": "Mesas y sillas modernas de vidrio y madera natural."
        },
        "proveedor": {
            "nombre_proveedor": "DecoHome S.A.S.",
            "telefono": "3157892345",
            "correo": "info@decohome.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=19HFES9IgfMxk2UWxKaKibsKMVdpKueep"
    },
    {
        "nombre_producto": "Lavadora Samsung Carga Frontal 22Kg Gris",
        "descripcion": "Lavadora Samsung con panel digital y sistema de lavado inteligente.",
        "descripcion_larga": "Lavadora automática de carga frontal Samsung con capacidad de 22 kg. Cuenta con motor Digital Inverter, múltiples programas de lavado y diseño moderno en color gris metálico.",
        "precio": 3299900,
        "marca": "Samsung",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Lavadoras automáticas de carga frontal."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroGlobal S.A.",
            "telefono": "3109876543",
            "correo": "ventas@electroglobal.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=16bjGSSLymM9IhQ49yLf29rhpIHkA-Cq-"
    },
    {
        "nombre_producto": "Lavadora Secadora LG WashTower Negra",
        "descripcion": "Centro de lavado LG con lavadora y secadora integradas en torre.",
        "descripcion_larga": "Sistema de lavado LG WashTower con capacidad combinada de 22 kg. Diseño vertical con lavadora y secadora independientes, panel de control central y conectividad ThinQ para control remoto.",
        "precio": 5899900,
        "marca": "LG",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Centros de lavado integrados con tecnología inteligente."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroGlobal S.A.",
            "telefono": "3109876543",
            "correo": "ventas@electroglobal.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1RL2lEM_DAeq_x2HVd1R5KKhPi6m42lvR"
    },
    {
        "nombre_producto": "Centro de Lavado Whirlpool Blanco 17Kg",
        "descripcion": "Centro de lavado con lavadora y secadora de carga superior.",
        "descripcion_larga": "Centro de lavado Whirlpool en color blanco con capacidad total de 17 kg. Incluye lavadora de carga superior y secadora eléctrica, ideal para espacios compactos.",
        "precio": 3899900,
        "marca": "Whirlpool",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Centros de lavado apilados y compactos para el hogar."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroGlobal S.A.",
            "telefono": "3109876543",
            "correo": "ventas@electroglobal.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1oTCZBR5d-SG5QAtW9gCSjvoxZo1Z99MY"
    },
    {
        "nombre_producto": "Televisor Samsung 50'' QLED 4K con Barra de Sonido",
        "descripcion": "Smart TV QLED 50 pulgadas con barra de sonido incluida.",
        "descripcion_larga": "Televisor Samsung QLED 4K de 50 pulgadas con tecnología Quantum HDR, control remoto solar y barra de sonido Bluetooth. Ideal para experiencias cinematográficas en casa.",
        "precio": 3199900,
        "marca": "Samsung",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Televisores inteligentes con barra de sonido."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroGlobal S.A.",
            "telefono": "3109876543",
            "correo": "ventas@electroglobal.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1BdVvD9vCT0cT_1MFhS0IViHU6ESnmy1F"
    },
    {
        "nombre_producto": "Televisor Smart TV challenger 55'' 4K Google TV",
        "descripcion": "Televisor inteligente challenger 4K con sistema operativo Google TV.",
        "descripcion_larga": "Smart TV challenger 55 pulgadas con resolución 4K UHD, HDR10, compatibilidad con Google Assistant y Chromecast integrado. Experiencia fluida y acceso directo a Netflix, Disney+ y YouTube.",
        "precio": 3599900,
        "marca": "challenger",
        "categoria": {
            "nombre_categoria_producto": "Electrodomésticos",
            "descripcion": "Televisores inteligentes con sistema Google TV."
        },
        "proveedor": {
            "nombre_proveedor": "ElectroGlobal S.A.",
            "telefono": "3109876543",
            "correo": "ventas@electroglobal.com"
        },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1yVyNx568rr_HtbpME2dM3Ps2A5wgA5j1"
    }
]