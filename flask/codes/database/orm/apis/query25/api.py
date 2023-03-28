from flask_restful import Resource

from repository import QueriesRepository


class Query25(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        users = queries_repo.query25()
        response = {
            'users': users
        }
        return response
