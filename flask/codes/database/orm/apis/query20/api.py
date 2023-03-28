from flask_restful import Resource

from apis.query20.validation import query20_parser
from repository import QueriesRepository


class Query20(Resource):
    parser = query20_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        price = args['price']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query20(price)
        response = {
            'items': items
        }
        return response
