from flask_restful import Resource

from repository import QueriesRepository


class Query8(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        items_details = queries_repo.query8()
        response = {
            'items_details': items_details
        }
        return response
