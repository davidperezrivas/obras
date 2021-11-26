from datetime import datetime
from server import db
import sqlalchemy as sa


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    rol_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    create_at = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime.utcnow,
        server_default=sa.func.now(),
    )
    update_at = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime.utcnow,
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
    )

    def __str__(self):
        return f"ID: {self.id}, nombre: {self.nombre}, apellido: {self.apellido}"
