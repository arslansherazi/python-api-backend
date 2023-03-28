from flask_restful import Resource

from apis.query10.validation import query10_parser
from repository import QueriesRepository


class Query10(Resource):
    parser = query10_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        records_limit = args['records_limit']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query10(records_limit)
        response = {
            'items': items
        }
        return response
