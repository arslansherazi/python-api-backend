from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# app configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/library_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
app.secret_key = 'HH234dDDii9087ttTyYuuUiopFFggHH23##$$%123wsdf'
