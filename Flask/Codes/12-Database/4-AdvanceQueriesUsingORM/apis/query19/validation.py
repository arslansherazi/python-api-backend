from flask_restful import reqparse


query19_parser = reqparse.RequestParser()

query19_parser.add_argument('items_count', required=True, type=int)
