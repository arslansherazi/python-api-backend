from flask_restful import reqparse


query26_parser = reqparse.RequestParser()

query26_parser.add_argument('customer_id', required=True, type=int)
query26_parser.add_argument('category', required=True, type=str)
