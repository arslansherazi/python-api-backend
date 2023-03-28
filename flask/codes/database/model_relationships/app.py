from flask import Flask

from flask_sqlalchemy import SQLAlchemy


# app configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://debian-sys-maint:eYkkCS20RRPsuvcO@localhost/practice_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
