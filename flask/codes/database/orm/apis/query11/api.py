from flask_restful import Resource

from apis.query11.validation import query11_parser
from repository import QueriesRepository


class Query11(Resource):
    parser = query11_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        price1 = args['price1']
        price2 = args['price2']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query11(price1, price2)
        response = {
            'items': items
        }
        return response
