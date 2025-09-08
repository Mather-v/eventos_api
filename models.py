from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EventoAcademico(db.Model):
    __tablename__ = 'eventos_academicos'  

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
