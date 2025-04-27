# Inventory System / Sistema de Inventario

Proyecto de práctica para gestionar inventario con Python, SQLite y Peewee.  
Practice project for managing inventory with Python, SQLite and Peewee.

## Cómo empezar / How to start

```bash
# Clona el repositorio / Clone the repo
git clone https://github.com/tu-usuario/inventory_system.git

# Entra en la carpeta del proyecto / Enter the project folder
cd inventory_system

# Crea y activa un entorno virtual / Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# Instala las dependencias / Install dependencies
pip install -r requirements.txt
```

## Estructura del proyecto / Project structure

```text
inventory_system/
├── inventory/              # Código con Peewee ORM / Code with Peewee ORM
│   ├── __init__.py
│   ├── database.py         # Conexión a SQLite / SQLite connection (ORM)
│   ├── models.py           # Definición de tablas / Table definitions (ORM)
│   ├── controllers.py      # Lógica de negocio / Business logic (ORM)
│   └── cli.py              # CLI interface (ORM)
│
├── raw_sql/                # Código “puro” sqlite3 / Raw sqlite3 code
│   ├── __init__.py
│   ├── db.py               # Conexión y setup con sqlite3 / sqlite3 connection & setup
│   ├── controllers.py      # Funciones CRUD manuales / Manual CRUD functions
│   └── cli.py              # CLI interface para raw_sql / CLI for raw_sql module
│   └── queries.py
├── tests/                  # Pruebas unitarias / Unit tests
│   ├── test_inventory.py   # (puedes separar tests ORM vs raw_sql si quieres)
│   └── test_raw_sql.py
│
├── .gitignore              # Ignorados / Ignored files and folders
├── README.md               # Documentación / Project documentation
└── requirements.txt        # Dependencias / Dependencies (Peewee, pytest…)


