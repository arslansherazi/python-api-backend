from flask_restful import Resource

from repository import QueriesRepository


class Query7(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        customers = queries_repo.query7()
        response = {
            'customers': customers
        }
        return response
