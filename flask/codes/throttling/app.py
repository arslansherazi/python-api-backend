from flask import Flask
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# app Configurations
app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/company_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mm = Marshmallow(app)
app.config['JWT_SECRET_KEY'] = 'HHjj222@@##fgdews123$$%%lloo00234df567KKLL//!!234rf'
jwt = JWTManager(app)
limiter = Limiter(app, key_func=get_remote_address)
