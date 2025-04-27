from peewee import (
    Model,
    AutoField,
    CharField,
    TextField,
    ForeignKeyField,
    DecimalField,
    DateTimeField
)

from .database import db


class UnidadMedida(Model):
    """
    Representa una unidad de medida, por ejemplo kilogramo o litro.   
    Represents a unit of measure, e.g., kilogram or liter.
    """
    id = AutoField()                    # ID único / Auto-increment ID
    # Nombre de la unidad / Unit name (e.g., "Kilogramo")
    nombre = CharField(unique=True)
    # Abreviatura de la unidad / Unit abbreviation (e.g., "kg", "L", "u")
    abreviatura = CharField()

    class Meta:
        """
        Meta datos para UnidadMedida: define la base de datos y el nombre de la tabla.  
        Meta data for UnidadMedida: defines the database and table name.
        """
        database = db
        table_name = "unidad_medida"


class Categoria(Model):
    """
    Agrupa productos según características comunes, como Frutos Secos.  
    Groups products by common features, such as nuts.
    """
    id = AutoField()                    # ID único / Auto-increment ID
    # Nombre de la categoría / Category name (e.g., "Frutos Secos")
    nombre = CharField(unique=True)
    # Descripción de la categoría / Category description
    descripcion = TextField(null=True)

    class Meta:
        """
        Meta datos para Categoria: define la base de datos y el nombre de la tabla.  
        Meta data for Categoria: defines the database and table name.
        """
        database = db
        table_name = "categoria"


class Proveedor(Model):
    """
    Información de contacto de proveedores de productos.  
    Contact information for product suppliers.
    """
    id = AutoField()                    # ID único / Auto-increment ID
    nombre = CharField(unique=True)     # Nombre del proveedor / Supplier name
    # Teléfono del proveedor / Supplier phone
    telefono = CharField(null=True)
    # Correo electrónico del proveedor / Supplier email
    email = CharField(null=True)
    # Dirección del proveedor / Supplier address
    direccion = TextField(null=True)
    # Página web del proveedor / Supplier website URL
    pagina_web = CharField(null=True)

    class Meta:
        """
        Meta datos para Proveedor: define la base de datos y el nombre de la tabla.  
        Meta data for Proveedor: defines the database and table name.
        """
        database = db
        table_name = "proveedor"


class Producto(Model):
    """
    Detalles de productos disponibles, vinculados a categoría y unidad de medida.  
    Details of available products, linked to category and unit of measure.
    """
    id = AutoField()                    # ID único / Auto-increment ID
    nombre = CharField(unique=True)     # Nombre del producto / Product name
    # Descripción del producto / Product description
    descripcion = TextField(null=True)
    # Precio por unidad en ARS / Unit price in ARS
    precio_unitario = DecimalField(10, 2)
    # Stock actual con decimales / Current stock with decimals
    stock = DecimalField(10, 3)
    categoria = ForeignKeyField(
        Categoria, backref="productos"
    )                                    # Categoría del producto / Product category
    unidad = ForeignKeyField(
        UnidadMedida, backref="productos"
        # Unidad de medida del producto / Product unit of measure
    )
    proveedor_principal = ForeignKeyField(
        Proveedor, backref="productos", null=True
        # Proveedor principal (opcional) / Main supplier (optional)
    )

    class Meta:
        """
        Meta datos para Producto: define la base de datos y el nombre de la tabla.  
        Meta data for Producto: defines the database and table name.
        """
        database = db
        table_name = "producto"


class Movimiento(Model):
    """
    Registro de entradas y salidas de stock de productos con timestamp.  
    Record of product stock in/out movements with timestamp.
    """
    id = AutoField()                    # ID único / Auto-increment ID
    producto = ForeignKeyField(
        Producto, backref="movimientos"
    )                                    # Producto asociado / Associated product
    # Cantidad movida con decimales / Moved quantity with decimals
    cantidad = DecimalField(10, 3)
    # Tipo de movimiento: 'in' o 'out' / Movement type: 'in' or 'out'
    tipo_movimiento = CharField()
    # Fecha y hora del movimiento / Movement timestamp
    fecha = DateTimeField()

    class Meta:
        """
        Meta datos para Movimiento: define la base de datos y el nombre de la tabla.  
        Meta data for Movimiento: defines the database and table name.
        """
        database = db
        table_name = "movimiento"
