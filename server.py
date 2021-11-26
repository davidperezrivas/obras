from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)
api = Api(app)


app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://david:david1995@localhost:3306/obras"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from src.usuarios.usuario_routes import usuarios

api.add_namespace(usuarios, path="/usuarios")

# db.drop_all()
# db.create_all()

migrate = Migrate(app, db)

