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
├── inventory/              # Código fuente / Source code
│   ├── __init__.py
│   ├── database.py         # Conexión a SQLite / SQLite connection
│   ├── models.py           # Definición de tablas / Table definitions
│   ├── controllers.py      # Lógica de negocio / Business logic
│   └── cli.py              # Interfaz de línea de comandos / CLI interface
├── tests/                  # Pruebas unitarias / Unit tests
├── .gitignore              # Ignorados / Ignored files and folders
├── README.md               # Documentación / Project documentation
└── requirements.txt        # Dependencias / Dependencies

