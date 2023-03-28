from flask_restful import reqparse


query18_parser = reqparse.RequestParser()

query18_parser.add_argument('item_id', required=True, type=int)
