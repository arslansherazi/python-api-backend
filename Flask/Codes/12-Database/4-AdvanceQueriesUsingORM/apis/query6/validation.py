from flask_restful import reqparse


query6_parser = reqparse.RequestParser()

query6_parser.add_argument('category', required=True, type=str)
