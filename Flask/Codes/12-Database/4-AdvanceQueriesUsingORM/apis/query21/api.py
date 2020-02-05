from flask_restful import Resource

from apis.query21.validation import query21_parser
from repository import QueriesRepository


class Query21(Resource):
    parser = query21_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        price = args['price']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query21(price)
        response = {
            'items': items
        }
        return response
