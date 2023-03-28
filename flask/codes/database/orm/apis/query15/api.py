from flask_restful import Resource

from repository import QueriesRepository


class Query15(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        orders = queries_repo.query15()
        response = {
            'orders': orders
        }
        return response
