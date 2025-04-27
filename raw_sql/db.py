# raw_sql/db.py

import sqlite3
from .queries import (
    UNIT_CREATE_SQL,
    CATEGORY_CREATE_SQL,
    PRODUCT_CREATE_SQL,
    MOVEMENT_CREATE_SQL
)

DB_PATH = "inventory.db"


def get_connection():
    """Abre y devuelve una conexión SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    """
    Crea las tablas unidad_medida, categoria,
    producto y movimiento si no existen.
    """
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(UNIT_CREATE_SQL)
            cur.execute(CATEGORY_CREATE_SQL)
            cur.execute(PRODUCT_CREATE_SQL)
            cur.execute(MOVEMENT_CREATE_SQL)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al inicializar la BD: {e}")


if __name__ == "__main__":
    initialize_database()
    print("Base de datos y tablas configuradas con éxito")
