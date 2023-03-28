from flask_restful import Resource

from repository import QueriesRepository


class Query17(Resource):
    def post(self):
        # get data from repository
        queries_repo = QueriesRepository()
        employees = queries_repo.query17()
        response = {
            'employees': employees
        }
        return response
