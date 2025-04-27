# 1. Tabla Unidad de Medida / Measurement Unit table
UNIT_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS unidad_medida (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    abreviatura TEXT NOT NULL
);
"""

# 2. Tabla Categoría / Category table
CATEGORY_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
);
"""

# 3. Tabla Producto / Product table
PRODUCT_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio_unitario REAL NOT NULL,
    stock REAL NOT NULL DEFAULT 0,
    categoria_id INTEGER NOT NULL,
    unidad_id INTEGER NOT NULL,
    FOREIGN KEY(categoria_id) REFERENCES categoria(id),
    FOREIGN KEY(unidad_id)    REFERENCES unidad_medida(id)
);
"""

# 4. Tabla Movimiento / Movement table
MOVEMENT_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS movimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    cantidad REAL NOT NULL,
    tipo_movimiento TEXT NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY(producto_id) REFERENCES producto(id)
);
"""

# --- CRUD unidad_medida ---
UNIT_INSERT_SQL = """
INSERT INTO unidad_medida (nombre, abreviatura)
VALUES (?, ?);
"""

UNIT_SELECT_ALL_SQL = """
SELECT * FROM unidad_medida;
"""

UNIT_SELECT_SQL = """
SELECT * FROM unidad_medida
WHERE id = ?;
"""

UNIT_UPDATE_SQL = """
UPDATE unidad_medida
SET nombre = ?, abreviatura = ?
WHERE id = ?;
"""

UNIT_DELETE_SQL = """
DELETE FROM unidad_medida
WHERE id = ?;
"""

# --- CRUD categoría ---
CATEGORY_INSERT_SQL = """
INSERT INTO categoria (nombre, descripcion)
VALUES (?, ?);
"""

CATEGORY_SELECT_ALL_SQL = """
SELECT * FROM categoria;
"""

CATEGORY_SELECT_SQL = """
SELECT * FROM categoria
WHERE id = ?;
"""

CATEGORY_UPDATE_SQL = """
UPDATE categoria
SET nombre = ?, descripcion = ?
WHERE id = ?;
"""

CATEGORY_DELETE_SQL = """
DELETE FROM categoria
WHERE id = ?;
"""

# --- CRUD producto ---
PRODUCT_INSERT_SQL = """
INSERT INTO producto (nombre, descripcion, precio_unitario, stock, categoria_id, unidad_id)
VALUES (?, ?, ?, ?, ?, ?);
"""

PRODUCT_SELECT_ALL_SQL = """
SELECT * FROM producto;
"""

PRODUCT_SELECT_SQL = """
SELECT * FROM producto
WHERE id = ?;
"""

PRODUCT_UPDATE_SQL = """
UPDATE producto
SET nombre = ?, descripcion = ?, precio_unitario = ?, stock = ?, categoria_id = ?, unidad_id = ?
WHERE id = ?;
"""

PRODUCT_DELETE_SQL = """
DELETE FROM producto
WHERE id = ?;
"""

# --- CRUD movimiento ---
MOVEMENT_INSERT_SQL = """
INSERT INTO movimiento (producto_id, cantidad, tipo_movimiento, fecha)
VALUES (?, ?, ?, ?);
"""

MOVEMENT_SELECT_ALL_SQL = """
SELECT * FROM movimiento
WHERE producto_id = ?;
"""

MOVEMENT_SELECT_SQL = """
SELECT * FROM movimiento
WHERE id = ?;
"""
