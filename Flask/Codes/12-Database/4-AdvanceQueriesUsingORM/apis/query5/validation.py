from flask_restful import reqparse


query5_parser = reqparse.RequestParser()

query5_parser.add_argument('category1', required=True, type=str)
query5_parser.add_argument('category2', required=True, type=str)
