from flask_restful import reqparse


query4_parser = reqparse.RequestParser()

query4_parser.add_argument('first_name', required=True, type=str)
query4_parser.add_argument('last_name', required=True, type=str)
