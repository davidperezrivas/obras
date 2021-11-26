from datetime import datetime
from server import db
import sqlalchemy as sa


class Rol(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False, unique=True)
    valor = db.Column(db.Integer, nullable=False, unique=True)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    roles = db.relationship("Usuario", backref="rol")
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
        return f"ID: {self.id}, nombre: {self.nombre}, valor: {self.valor}, estado: {self.estado}"
