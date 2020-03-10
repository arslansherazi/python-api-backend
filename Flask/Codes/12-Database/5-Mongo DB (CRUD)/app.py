from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api


# app configurations
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'students_db',
    'host': 'localhost',
    'port': 27017
}
mongo_db = MongoEngine(app)
api = Api(app)
