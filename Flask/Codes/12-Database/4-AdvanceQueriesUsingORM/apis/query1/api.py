from flask_restful import Resource

from repository import QueriesRepository


class Query1(Resource):
    def get(self):
        # get data from repository
        queries_repo = QueriesRepository()
        customers = queries_repo.query1()
        response = {
            'customers': customers
        }
        return response
