from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query16(APIView):
    def get(self, request):
        queries_repo = QueriesRepository()
        employees = queries_repo.query16()
        response = {
            'employees': employees
        }
        return Response(response)
