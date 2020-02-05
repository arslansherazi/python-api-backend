from flask_restful import reqparse


query21_parser = reqparse.RequestParser()

query21_parser.add_argument('price', required=True, type=int)
