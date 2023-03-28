from flask_restful import Resource

from apis.query5.validation import query5_parser
from repository import QueriesRepository


class Query5(Resource):
    parser = query5_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        category1 = args['category1']
        category2 = args['category2']

        # get data from repository
        queries_repo = QueriesRepository()
        items_names = queries_repo.query5(category1, category2)
        response = {
            'items_names': items_names
        }
        return response
