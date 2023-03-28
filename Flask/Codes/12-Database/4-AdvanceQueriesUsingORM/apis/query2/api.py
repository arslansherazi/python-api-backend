from flask_restful import Resource

from repository import QueriesRepository
from apis.query2.validation import query2_parser


class Query2(Resource):
    parser = query2_parser

    def post(self):
        # get request arguments
        args = self.parser.parse_args()
        cnic_no = args['cnic_no']

        # get data from repository
        queries_repo = QueriesRepository()
        customer = queries_repo.query2(cnic_no)
        response = {
            'customer': customer
        }
        return response
