from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# app Configurations
app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/student_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mm = Marshmallow(app)

