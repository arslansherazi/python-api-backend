from flask_restful import reqparse


query12_parser = reqparse.RequestParser()

query12_parser.add_argument('category', required=True, type=str)
