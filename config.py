import os

class Config:
    # Clave secreta (se usa para sesiones, seguridad, etc.)
    SECRET_KEY = os.environ.get("SECRET_KEY") or "clave_segura_secreta_realista"

    # Configuración de la base de datos (por ahora SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///eventos.db"

    # Evita warnings innecesarios de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False



