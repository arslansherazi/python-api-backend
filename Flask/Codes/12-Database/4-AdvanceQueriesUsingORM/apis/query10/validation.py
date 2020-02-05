from flask_restful import reqparse


query10_parser = reqparse.RequestParser()

query10_parser.add_argument('records_limit', required=True, type=int)
