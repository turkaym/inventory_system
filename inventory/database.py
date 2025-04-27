from peewee import SqliteDatabase
from .models import UnidadMedida, Categoria, Proveedor, Producto, Movimiento

DB_NAME = "inventory.db"  # Archivo de la base de datos / Database file name
db = SqliteDatabase(DB_NAME)  # Objeto de conexión / Connection object


def initialize_database():
    """
    Conecta y crea las tablas si no existen /
    Connects and creates tables if they don't exist.
    """
    # db.connect(reuse_if_open=True)  # Opción: solo si quieres evitar reconexiones
    db.connect()
    db.create_tables(
        [UnidadMedida, Categoria, Proveedor, Producto, Movimiento])
    db.close()
