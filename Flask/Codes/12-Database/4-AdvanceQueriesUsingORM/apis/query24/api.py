from flask_restful import Resource

from repository import QueriesRepository


class Query24(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        items = queries_repo.query24()
        response = {
            'items': items
        }
        return response
