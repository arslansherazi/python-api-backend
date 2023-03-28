from flask_restful import Resource

from apis.query6.validation import query6_parser
from repository import QueriesRepository


class Query6(Resource):
    parser = query6_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        category = args['category']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query6(category)
        response = {
            'items': items
        }
        return response
