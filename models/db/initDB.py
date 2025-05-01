import sqlite3

# Esto crea el archivo si no existe
conn = sqlite3.connect("punto_venta.db")

# Crear tabla (opcional)
cursor = conn.cursor()

cursor.executescript('''

  CREATE TABLE codigo_ventas (
    id INTEGER PRIMARY KEY,
    codigo_venta TEXT NOT NULL,
    total_pagado REAL NOT NULL,
    fecha TEXT NOT NULL DEFAULT (DATE('now', 'localtime'))
  );

  CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    codigo_barras TEXT NOT NULL,
    nombre TEXT NOT NULL,
    typo INTEGER NOT NULL DEFAULT 0,
    precio REAL NOT NULL,
    gramaje INTEGER NOT NULL,
    cantidad_contable INTEGER NOT NULL
  );

  INSERT INTO productos (id, codigo_barras, nombre, typo, precio, gramaje, cantidad_contable) VALUES
  (1, '', 'Manzanas', 2, 30, 5000, 0),
  (2, '', 'Naranjas', 2, 1.2, 1000, 0),
  (3, '', 'Plátanos', 2, 20, 800, 0),
  (4, '', 'Aguacates', 2, 2.5, 400, 0),
  (5, '', 'Papas', 2, 0.8, 1000, 0),
  (6, '', 'Cebollas', 2, 0.9, 500, 0),
  (7, '', 'Tomates', 2, 1.3, 600, 0),
  (8, '', 'Zanahorias', 2, 1, 700, 0),
  (9, '', 'Frijoles a granel', 2, 2, 1200, 0),
  (10, '', 'Arroz a granel', 2, 1.8, 1500, 0),
  (11, '', 'Azúcar a granel', 2, 1.6, 1000, 0),
  (12, '', 'Sal a granel', 2, 0.5, 500, 0),
  (13, '', 'Harina a granel', 2, 1.4, 2000, 0),
  (14, '', 'Queso fresco', 2, 3, 250, 0),
  (15, '', 'Pollo en piezas', 2, 3.5, 1200, 0),
  (16, '', 'Carne molida', 2, 4, 1000, 0),
  (17, '', 'Chuletas de cerdo', 2, 4.5, 900, 0),
  (18, '', 'Filete de pescado', 2, 5, 800, 0),
  (19, '', 'Huevos por kilo', 2, 2.5, 1200, 0),
  (20, '', 'Mantequilla a granel', 2, 2, 500, 0),
  (21, '', 'Paquete de galletas', 1, 1, 0, 2),
  (22, '', 'Caja de leche', 1, 1.5, 0, 1),
  (23, 'JM03NZ0080055Q8FAH0S', 'Pan de caja', 1, 2, 0, 1),
  (24, '', 'Refresco de 2L', 1, 1.8, 0, 1),
  (25, '', 'Refresco de 600ml', 1, 1, 0, 1),
  (26, '', 'Botella de agua 1L', 1, 0.8, 0, 1),
  (27, '', 'Papel higienico 4 rollos', 1, 3.5, 0, 1),
  (28, '', 'Shampoo 500ml', 1, 4, 0, 1),
  (29, '', 'Jabon de barra', 1, 0.5, 0, 3),
  (30, '', 'Caja de cereal', 1, 3, 0, 1),
  (31, '', 'Salsa en botella', 1, 1.5, 0, 1),
  (32, '', 'Mayonesa 500g', 1, 2, 0, 1),
  (33, '', 'Mostaza 200g', 1, 1, 0, 1),
  (34, '', 'Aceite de cocina 1L', 1, 3, 0, 1),
  (35, '', 'Detergente en polvo 1kg', 1, 4, 0, 1),
  (36, '', 'Esponjas para trastes', 1, 1.2, 0, 2),
  (37, '', 'Cajas de cerillos', 1, 0.5, 0, 3),
  (38, '', 'Bolsa de frituras', 1, 1, 0, 1),
  (39, '', 'Chocolate en barra', 1, 1.5, 0, 1),
  (40, '', 'Chicles paquete', 1, 0.8, 0, 5),
  (41, '', 'Té en caja', 1, 2, 0, 1),
  (42, '', 'Café soluble 200g', 1, 3.5, 0, 1),
  (48, 'dasdasdasd', 'PRODUCTO EDITADO', 1, 65, 0, 62);

  CREATE TABLE typo_productos (
    id INTEGER PRIMARY KEY,
    typo TEXT NOT NULL
  );

  INSERT INTO typo_productos (id, typo) VALUES
  (1, 'contable'),
  (2, 'gramaje');

  CREATE TABLE typo_usuarios (
    id INTEGER PRIMARY KEY,
    typo TEXT NOT NULL
  );

  INSERT INTO typo_usuarios (id, typo) VALUES
  (1, 'empleado'),
  (2, 'administrador');

  CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    usuario TEXT NOT NULL,
    typo INTEGER NOT NULL,
    password TEXT NOT NULL
  );

  INSERT INTO usuarios (id, usuario, typo, password) VALUES
  (1, 'Iniciador', 2, '');

  CREATE TABLE ventas (
    id INTEGER PRIMARY KEY,
    codigo_venta INTEGER NOT NULL DEFAULT 0,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    typo INTEGER NOT NULL,
    gramaje INTEGER NOT NULL,
    precio_acumulado REAL NOT NULL
  );
  
''')



conn.commit()
conn.close()
