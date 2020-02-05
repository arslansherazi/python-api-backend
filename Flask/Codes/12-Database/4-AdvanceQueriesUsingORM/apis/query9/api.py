from flask_restful import Resource

from repository import QueriesRepository


class Query9(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        customers = queries_repo.query9()
        response = {
            'customers': customers
        }
        return response
