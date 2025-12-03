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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1oTCZBR5d-SG5QAtW9gCSjvoxZo1Z99MY"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1BdVvD9vCT0cT_1MFhS0IViHU6ESnmy1F"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1yVyNx568rr_HtbpME2dM3Ps2A5wgA5j1"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=19HFES9IgfMxk2UWxKaKibsKMVdpKueep"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=16bjGSSLymM9IhQ49yLf29rhpIHkA-Cq-"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1RL2lEM_DAeq_x2HVd1R5KKhPi6m42lvR"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1uDESXXakDCk_ZCyyAMrGfwteO69OqfXI"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1DAs17QpW1iiONXZS3z7Qtzj9qJCgYH9d"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1aGYilt9Ix7O0nyKzV2kFiQRfc84OA2i9"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1K94LZNclNhqHuzgwYRO0XCrUWaE5_Vbu"
    }
    {
        "nombre_producto": "Estufa Empotrable 5 Quemadores Vidrio Negro",
        "descripcion": "Cubierta a gas de 5 quemadores con parrillas en hierro fundido.",
        "descripcion_larga": "Cubierta empotrable en vidrio templado negro con 5 quemadores, incluyendo quemador central de alta potencia. Parrillas en hierro fundido, perillas frontales metálicas y encendido eléctrico. Diseño moderno para cocinas integrales.",
        "precio": 1199900,
        "marca": "Indurama",
        "categoria": { "nombre_categoria_producto": "Cocinas y Empotrables", "descripcion": "Cubiertas, hornos y campanas." },
        "proveedor": { "nombre_proveedor": "ElectroDistribuciones S.A.", "telefono": "3124567890", "correo": "contacto@electrodistribuciones.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1PRszugOUXtHvHpG6osKaC_poZ4plglKG"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1f4otmIwmYQ5vye-y4mitcu4fjOs42OVc"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1N5JYjnSum3rbLf2bTgtTxUrGD2bPauY1"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1IjoBnXaPFyU6FOxCQV9wVrGqyJryPW_x"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1jOM6FwvSy3lbzldrbkUoytpPHiANQM1S"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=168yu5R-f_UziUxAglL19A6uKxmGi-BkP"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1_TGyoMQtiGBF4GHr6n9FSgF-4fe14xC_"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1313m53WwZavTVe8VIgbOqZ4tC0suIPQZ"
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
        "imagen_principal": "https://drive.google.com/uc?export=download&id=1jtFdGDSFIeiu8b1oRS_QiWUpdCfLrMfn"
    },
    # 20) Congelador/Refrigerador vertical (Challenger)
    {
        "nombre_producto": "Congelador Vertical 180 L Inox",
        "descripcion": "Electrodoméstico vertical de bajo consumo en acero.",
        "descripcion_larga": "Congelador vertical de 180 litros con puerta en acero inoxidable, control de temperatura y bandejas internas. Ideal para cocinas pequeñas o áreas auxiliares.",
        "precio": 1399900,
        "marca": "Challenger",
        "categoria": { "nombre_categoria_producto": "Electrodomésticos", "descripcion": "Refrigeración y congelación." },
        "proveedor": { "nombre_proveedor": "ElectroDistribuciones S.A.", "telefono": "3124567890", "correo": "contacto@electrodistribuciones.com" },
        "imagen_principal": "https://drive.google.com/uc?export=download&id=19lgJalewSYc4ZjgIdUny5KuuvZ2unbdV"
    },
    {
        "nombre": "Congelador Horizontal Industrial Vidrio Corredizo",
        "descripcion_corta": "Congelador horizontal con tapa de vidrio corredizo, ideal para comercios.",
        "descripcion_larga": "Congelador horizontal industrial con tapa de vidrio corredizo. Ofrece gran capacidad de almacenamiento y eficiencia energética. Ideal para negocios, tiendas y hogares que requieren conservación prolongada de alimentos congelados. Su diseño facilita la visualización del contenido sin pérdida de frío.",
        "categoria": "Electrodomésticos",
        "marca": "Indufrial",
        "proveedor": "Proveedor Genérico",
        "precio": 1299000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Lavavajillas Empotrable Acero Inoxidable",
        "descripcion_corta": "Lavavajillas empotrable con bandejas dobles metálicas.",
        "descripcion_larga": "Lavavajillas empotrable en acero inoxidable con dos bandejas deslizables, diseño silencioso y eficiente. Incluye sistema avanzado de lavado con múltiples ciclos, ahorro de agua y energía. Ideal para cocinas modernas que requieren practicidad y alto rendimiento.",
        "categoria": "Electrodomésticos",
        "marca": "Samsung",
        "proveedor": "Proveedor Genérico",
        "precio": 2399000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Silla de Oficina Ergonómica Respaldo Malla Negra",
        "descripcion_corta": "Silla de oficina ergonómica con respaldo en malla y asiento acolchado.",
        "descripcion_larga": "Silla de oficina ergonómica con respaldo en malla transpirable, asiento acolchado de alta densidad y base con ruedas de giro suave. Incluye ajuste de altura y reposabrazos fijos. Ideal para jornadas largas de trabajo gracias a su soporte lumbar natural.",
        "categoria": "Muebles de Oficina",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 229000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Silla Gamer Profesional Blanco y Negro",
        "descripcion_corta": "Silla gamer reclinable con diseño deportivo.",
        "descripcion_larga": "Silla gamer ergonómica con diseño deportivo en colores blanco y negro. Incluye reclinación, cojín lumbar, almohada cervical y reposapiés retráctil. Fabricada en cuero sintético de alta resistencia y base metálica. Ideal para gaming, oficina o estudio.",
        "categoria": "Muebles de Oficina",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 499000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Silla Ejecutiva Ergonómica Gris con Cabecero",
        "descripcion_corta": "Silla ejecutiva con cabecero y respaldo en malla gris.",
        "descripcion_larga": "Silla ejecutiva ergonómica con respaldo de malla gris, asiento acolchado, cabecero ajustable y base cromada. Ofrece soporte lumbar adecuado y excelente ventilación, ideal para ambientes laborales modernos.",
        "categoria": "Muebles de Oficina",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 389000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Silla de Oficina Gris Claro con Cabecero Blanco",
        "descripcion_corta": "Silla de oficina moderna con cabecero blanco y respaldo en malla.",
        "descripcion_larga": "Silla ergonómica con diseño moderno en tonos gris claro y blanco. Incluye cabecero, respaldo en malla, asiento acolchado y base cromada. Ofrece comodidad y estilo para oficinas contemporáneas.",
        "categoria": "Muebles de Oficina",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 359000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Pintura Viniltex Advanced Mate 5 Galones",
        "descripcion_corta": "Pintura para interiores Viniltex formato 5 galones.",
        "descripcion_larga": "Pintura Viniltex Advanced Mate de alto rendimiento ideal para paredes interiores. Ofrece excelente cubrimiento, fácil limpieza, máxima lavabilidad y alta durabilidad. Elimina hasta el 99% de bacterias y proporciona acabado mate profesional.",
        "categoria": "Pinturas",
        "marca": "Pintuco",
        "proveedor": "Proveedor Genérico",
        "precio": 239000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Pintura Topex Pro2000 5 Galones",
        "descripcion_corta": "Pintura blanca contratista, alto poder cubriente.",
        "descripcion_larga": "Pintura TopEx Pro2000 color blanco mate, ideal para contratistas y proyectos profesionales. Ofrece alto cubrimiento, fácil aplicación y excelente rendimiento. Formato de 5 galones, diseñada para uso interior.",
        "categoria": "Pinturas",
        "marca": "Topex",
        "proveedor": "Proveedor Genérico",
        "precio": 199900,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Pintura Viniltex Advanced Mate (Presentación Regular)",
        "descripcion_corta": "Pintura Viniltex interior en acabado mate.",
        "descripcion_larga": "Viniltex Advanced Mate con excelente cubrimiento, fácil lavado y durabilidad superior. Apta para paredes interiores con acabado profesional y gran rendimiento. Ideal para hogares, oficinas y remodelaciones.",
        "categoria": "Pinturas",
        "marca": "Pintuco",
        "proveedor": "Proveedor Genérico",
        "precio": 219900,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Escritorio con Repisas Laterales Madera Clara",
        "descripcion_corta": "Escritorio funcional con repisas y superficie blanca.",
        "descripcion_larga": "Escritorio moderno con estructura en madera clara y superficie blanca. Incluye repisas laterales para libros, decoración o almacenamiento. Ideal para estudio, oficina en casa o espacios juveniles.",
        "categoria": "Muebles",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 329000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Mueble de Cocina Modular Combo Alto y Bajo",
        "descripcion_corta": "Juego de muebles de cocina con módulos altos y bajos en madera clara y negro.",
        "descripcion_larga": "Conjunto modular de cocina compuesto por mueble alto con repisas abiertas, módulo superior doble y mueble inferior con lavaplatos integrado. Diseño moderno en madera clara con estructura negra. Ideal para optimizar espacios y añadir almacenamiento funcional en la cocina.",
        "categoria": "Muebles",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 1299000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Mueble de Cocina Modular en L con Gabinetes Superiores",
        "descripcion_corta": "Juego de cocina modular en L con múltiples gabinetes y estructura robusta.",
        "descripcion_larga": "Sistema modular de cocina con diseño en L que incluye varios gabinetes inferiores para ollas y utensilios, así como alacenas superiores con puertas y estante abierto. Su acabado en madera clara y negro aporta un estilo contemporáneo y funcional.",
        "categoria": "Muebles",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 1699000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Comedor 6 Puestos Moderno en Vidrio y Sillas Negras",
        "descripcion_corta": "Comedor moderno de 6 puestos con mesa de vidrio y sillas acolchadas negras.",
        "descripcion_larga": "Juego de comedor moderno compuesto por mesa rectangular con superficie de vidrio negro y seis sillas acolchadas en cuero sintético negro. Diseño elegante y minimalista que combina con interiores contemporáneos y espacios luminosos.",
        "categoria": "Muebles",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 879000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Comedor 6 Puestos con Mesa Madera Patrones Geométricos",
        "descripcion_corta": "Comedor contemporáneo con mesa de madera y sillas tapizadas.",
        "descripcion_larga": "Mesa rectangular en acabado de madera con patrones geométricos y seis sillas tapizadas en tonos verdes y grises. Comedor de estilo moderno con gran confort y estética sofisticada para hogares contemporáneos.",
        "categoria": "Muebles",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 1149000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Comedor 4 Puestos Mesa en Vidrio y Sillas Blancas",
        "descripcion_corta": "Comedor compacto con mesa de vidrio y sillas blancas de diseño nórdico.",
        "descripcion_larga": "Juego de comedor con mesa rectangular de vidrio templado y cuatro sillas blancas con patas de madera estilo escandinavo. Perfecto para espacios pequeños y decoración moderna, proporcionando elegancia y funcionalidad.",
        "categoria": "Muebles",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 599000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Lavadora Samsung Carga Frontal Gris 20 kg",
        "descripcion_corta": "Lavadora Samsung de carga frontal color gris con panel digital.",
        "descripcion_larga": "Lavadora de carga frontal Samsung con capacidad aproximada de 20 kg. Incluye panel digital, múltiples ciclos de lavado, diseño moderno en acero gris y alta eficiencia energética. Ideal para hogares con alto volumen de ropa.",
        "categoria": "Electrodomésticos",
        "marca": "Samsung",
        "proveedor": "Proveedor Genérico",
        "precio": 2499000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Centro de Lavado LG Torre Lavadora + Secadora",
        "descripcion_corta": "Sistema vertical LG con lavadora y secadora integradas.",
        "descripcion_larga": "Centro de lavado vertical de LG compuesto por una lavadora de carga frontal en la parte inferior y secadora en la parte superior. Diseño compacto, moderno y de alta eficiencia, ideal para optimizar espacio en apartamentos o áreas pequeñas.",
        "categoria": "Electrodomésticos",
        "marca": "LG",
        "proveedor": "Proveedor Genérico",
        "precio": 5899000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Centro de Lavado Whirlpool Blanco Lavadora + Secadora",
        "descripcion_corta": "Centro de lavado Whirlpool con lavadora inferior y secadora superior.",
        "descripcion_larga": "Centro de lavado de la marca Whirlpool en diseño blanco tradicional. Incluye lavadora de carga superior en la parte inferior y secadora frontal arriba. Es una solución eficiente y compacta para espacios reducidos.",
        "categoria": "Electrodomésticos",
        "marca": "Whirlpool",
        "proveedor": "Proveedor Genérico",
        "precio": 3799000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Televisor Samsung QLED 50'' + Barra de Sonido",
        "descripcion_corta": "Smart TV QLED Samsung de 50 pulgadas con barra de sonido incluida.",
        "descripcion_larga": "Televisor Samsung QLED de 50 pulgadas con control solar, resolución avanzada y colores vibrantes. Incluye barra de sonido para mejorar la experiencia audiovisual. Ideal para salas modernas y entretenimiento en casa.",
        "categoria": "Tecnología",
        "marca": "Samsung",
        "proveedor": "Proveedor Genérico",
        "precio": 2999000,
        "imagen": "URL_PENDIENTE"
    },
    {
        "nombre": "Televisor Android TV 50'' Pantalla UHD",
        "descripcion_corta": "Smart TV UHD de 50 pulgadas con sistema Google TV.",
        "descripcion_larga": "Televisor de 50 pulgadas con sistema operativo Google TV. Incluye aplicaciones como Netflix, YouTube, Disney+, Prime Video y más. Pantalla UHD de alta definición ideal para entretenimiento y streaming.",
        "categoria": "Tecnología",
        "marca": "Genérica",
        "proveedor": "Proveedor Genérico",
        "precio": 1699000,
        "imagen": "URL_PENDIENTE"
    },
    {
      "nombre": "Escritorio en L moderno con estantería",
      "categoria": "muebles",
      "descripcion": "Escritorio en L con combinación de colores negro y madera natural, incluye estantería lateral con compartimientos y puerta abatible.",
      "precio": 599000,
      "stock": 10,
      "imagen": "LINK_29",
      "caracteristicas": [
        "Material: Madera MDF",
        "Color: Negro y roble",
        "Incluye estantes laterales",
        "Diseño moderno en L"
      ]
    },
    {
      "nombre": "Escritorio de vidrio con estructura metálica",
      "categoria": "muebles",
      "descripcion": "Escritorio con estructura metálica cromada y superficie de vidrio templado, ideal para espacios modernos y oficinas en casa.",
      "precio": 499000,
      "stock": 15,
      "imagen": "LINK_30",
      "caracteristicas": [
        "Superficie de vidrio templado",
        "Estructura metálica",
        "Diseño moderno",
        "Fácil de limpiar"
      ]
    },
    {
      "nombre": "Escritorio blanco con biblioteca integrada",
      "categoria": "muebles",
      "descripcion": "Escritorio compacto color blanco con biblioteca lateral de 4 niveles y espacio para computador.",
      "precio": 579000,
      "stock": 18,
      "imagen": "LINK_31",
      "caracteristicas": [
        "Material: MDP laminado",
        "Color blanco",
        "Incluye biblioteca lateral",
        "Amplio espacio para PC"
      ]
    },
    {
      "nombre": "Biblioteca alta 5 niveles color madera",
      "categoria": "muebles",
      "descripcion": "Biblioteca alta en acabado madera con cinco niveles de almacenamiento ideal para libros y decoración.",
      "precio": 329000,
      "stock": 20,
      "imagen": "LINK_32",
      "caracteristicas": [
        "5 niveles de almacenamiento",
        "Acabado color madera",
        "Diseño moderno",
        "Material MDP resistente"
      ]
    },
    {
      "nombre": "Estantería cuadrada blanca 9 compartimentos",
      "categoria": "muebles",
      "descripcion": "Estantería modular de nueve compartimientos en acabado blanco ideal para organización y decoración.",
      "precio": 259000,
      "stock": 25,
      "imagen": "LINK_33",
      "caracteristicas": [
        "9 compartimientos",
        "Color blanco",
        "Ideal para organización",
        "Material MDF"
      ]
    },
    {
      "nombre": "Biblioteca decorativa blanca",
      "categoria": "muebles",
      "descripcion": "Estantería decorativa blanca de diseño minimalista, perfecta para salas, oficinas o estudios.",
      "precio": 349000,
      "stock": 12,
      "imagen": "LINK_34",
      "caracteristicas": [
        "Diseño minimalista",
        "Material MDF",
        "6 compartimientos",
        "Color blanco mate"
      ]
    },
    {
      "nombre": "Estantería 9 cubos con canastas organizadoras",
      "categoria": "muebles",
      "descripcion": "Biblioteca de nueve cubos en color blanco, incluye canastas grises para mejorar el almacenamiento.",
      "precio": 289000,
      "stock": 14,
      "imagen": "LINK_35",
      "caracteristicas": [
        "Incluye 4 canastas organizadoras",
        "Color blanco con gris",
        "Material MDF",
        "Ideal para dormitorios u oficinas"
      ]
    },
    {
      "nombre": "Mueble inferior de cocina 5 puertas 1 cajón",
      "categoria": "muebles",
      "descripcion": "Mueble inferior de cocina con 5 puertas, 1 cajón y espacio para fregadero y estufa.",
      "precio": 659000,
      "stock": 10,
      "imagen": "LINK_36",
      "caracteristicas": [
        "Material MDP 15 mm",
        "5 puertas y 1 cajón",
        "Color blanco y madera",
        "Patas metálicas"
      ]
    },
    {
      "nombre": "Cocina modular en L color madera",
      "categoria": "muebles",
      "descripcion": "Cocina modular completa en forma de L, incluye gabinetes superiores e inferiores en acabado madera.",
      "precio": 1399000,
      "stock": 5,
      "imagen": "LINK_37",
      "caracteristicas": [
        "Diseño en L",
        "Muebles superiores e inferiores",
        "Acabado madera",
        "Amplio espacio de almacenamiento"
      ]
    },
    {
      "nombre": "Cocina integral moderna beige y madera",
      "categoria": "muebles",
      "descripcion": "Cocina integral moderna con mueble superior beige y mueble inferior en madera con superficie de acero.",
      "precio": 1199000,
      "stock": 8,
      "imagen": "LINK_38",
      "caracteristicas": [
        "Incluye gabinete superior",
        "Cubierta en acero",
        "Color beige y madera",
        "Espacio para lavaplatos y estufa"
      ]
    }
]

db.producto.insert_many(productos)
print("Productos insertados correctamente.")
