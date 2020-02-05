from flask_restful import reqparse


query22_parser = reqparse.RequestParser()

query22_parser.add_argument('price', required=True, type=int)
