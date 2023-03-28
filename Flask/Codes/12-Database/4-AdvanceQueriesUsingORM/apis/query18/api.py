from flask_restful import Resource

from apis.query18.validation import query18_parser
from repository import QueriesRepository


class Query18(Resource):
    parser = query18_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        item_id = args['item_id']

        # get data from repository
        queries_repo = QueriesRepository()
        item = queries_repo.query18(item_id)
        response = {
            'item': item
        }
        return response
