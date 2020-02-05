from flask_restful import reqparse


query20_parser = reqparse.RequestParser()

query20_parser.add_argument('price', required=True, type=int)
