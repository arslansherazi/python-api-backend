from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# app configurations
app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://debian-sys-maint:eYkkCS20RRPsuvcO@localhost/practice_db'
