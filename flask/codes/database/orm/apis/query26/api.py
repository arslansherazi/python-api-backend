from flask_restful import Resource

from apis.query26.validation import query26_parser
from repository import QueriesRepository


class Query26(Resource):
    parser = query26_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        customer_id = args['customer_id']
        category = args['category']

        # get data from repository
        queries_repo = QueriesRepository()
        customer_orders_information = queries_repo.query26(customer_id, category)
        response = {
            'customer_orders_information': customer_orders_information
        }
        return response
