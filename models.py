from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy import Enum


db = SQLAlchemy()


class CategoriaEvento(enum.Enum):
    CIBERSEGURIDAD = "Ciberseguridad"
    IA = "Inteligencia Artificial"
    REDES = "Redes"
    BASE_DATOS = "Bases de Datos"


class CategoriaRol(enum.Enum):
    PONENTE = "Ponente"
    ORGANIZADOR = "Organizador"
    INVITADO = "Invitado"
    

class EventoAcademico(db.Model):
    __tablename__ = 'eventos_academicos'  

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    categoria = db.Column(Enum(CategoriaEvento), nullable=False)


class Estudiantes(db.Model):
    __tablename__ = 'estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False)


class Profesores(db.Model):
    __tablename__ = 'profesores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


class Inscripciones(db.Model):
    __tablename__ = 'inscripciones'
    
    id = db.Column(db.Integer, primary_key=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos_academicos.id'), nullable=False)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiantes.id'), nullable=False)
    fecha_inscripcion = db.Column(db.Date, nullable=False)
    asistio = db.Column(db.Boolean, nullable=False, default=False)
    calificacion = db.Column(db.Boolean, nullable=False, default=False)


class ProfesorEvento(db.Model):
    __tablename__ = 'profesor_evento'

    id = db.Column(db.Integer, primary_key=True)
    id_profesor = db.Column(db.Integer, db.ForeignKey('profesores.id'), nullable=False)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos_academicos.id'), nullable=False)
    rol = db.Column(Enum(CategoriaRol), nullable=False)

