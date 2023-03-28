from flask_restful import reqparse


query23_parser = reqparse.RequestParser()

query23_parser.add_argument('price', required=True, type=int)
