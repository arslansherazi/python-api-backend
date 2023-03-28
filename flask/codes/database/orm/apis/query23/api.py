from flask_restful import Resource

from apis.query23.validation import query23_parser
from repository import QueriesRepository


class Query23(Resource):
    parser = query23_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        price = args['price']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query23(price)
        response = {
            'items': items
        }
        return response
