from flask_restful import Resource

from repository import QueriesRepository


class Query16(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        employees = queries_repo.query16()
        response = {
            'employees': employees
        }
        return response
