from flask_restful import Resource

from repository import QueriesRepository


class Query13(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        orders = queries_repo.query13()
        response = {
            'orders': orders
        }
        return response