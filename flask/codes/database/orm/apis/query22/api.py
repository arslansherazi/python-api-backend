from flask_restful import Resource

from apis.query22.validation import query22_parser
from repository import QueriesRepository


class Query22(Resource):
    parser = query22_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        price = args['price']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query22(price)
        response = {
            'items': items
        }
        return response
