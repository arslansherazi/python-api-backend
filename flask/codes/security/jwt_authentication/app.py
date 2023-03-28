from flask import Flask
from flask_jwt_extended import JWTManager

from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# app configurations
app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/students_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mm = Marshmallow(app)
app.config['JWT_SECRET_KEY'] = 'HHjj222@@##fgdews123$$%%lloo00234df567KKLL//!!234rf'
jwt = JWTManager(app)
