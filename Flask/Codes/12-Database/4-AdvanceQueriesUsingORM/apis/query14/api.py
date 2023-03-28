from flask_restful import Resource

from repository import QueriesRepository


class Query14(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        orders_items = queries_repo.query14()
        response = {
            'orders_items': orders_items
        }
        return response
