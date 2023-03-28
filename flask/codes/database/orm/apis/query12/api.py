from flask_restful import Resource

from apis.query12.validation import query12_parser
from repository import QueriesRepository


class Query12(Resource):
    parser = query12_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        category = args['category']

        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query12(category)
        response = {
            'items': items
        }
        return response
