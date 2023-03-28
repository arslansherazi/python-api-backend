from flask_restful import Resource

from apis.query4.validation import query4_parser
from repository import QueriesRepository


class Query4(Resource):
    parser = query4_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        first_name = args['first_name']
        last_name = args['last_name']

        # get data from repository
        queries_repo = QueriesRepository()
        customers = queries_repo.query4(first_name, last_name)
        response = {
            'customers': customers
        }
        return response
