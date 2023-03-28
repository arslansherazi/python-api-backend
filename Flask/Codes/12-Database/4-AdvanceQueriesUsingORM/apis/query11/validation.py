from flask_restful import reqparse


query11_parser = reqparse.RequestParser()

query11_parser.add_argument('price1', required=True, type=int)
query11_parser.add_argument('price2', required=True, type=int)
