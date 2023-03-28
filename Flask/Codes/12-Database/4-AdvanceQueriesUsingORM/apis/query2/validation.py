from flask_restful import reqparse


query2_parser = reqparse.RequestParser()

query2_parser.add_argument('cnic_no', required=True, type=int)
