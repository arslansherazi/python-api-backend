from flask_restful import Resource

from apis.query19.validation import query19_parser
from repository import QueriesRepository


class Query19(Resource):
    parser = query19_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        items_count = args['items_count']

        # get data from repository
        queries_repo = QueriesRepository()
        items_count = queries_repo.query19(items_count)
        response = {
            'items_count': items_count
        }
        return response
