from flask_restful import Resource

from repository import QueriesRepository


class Query3(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        item_categories = queries_repo.query3()
        response = {
            'item_categories': item_categories
        }
        return response
