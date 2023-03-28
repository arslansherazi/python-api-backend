from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query9(APIView):
    def get(self, request):
        queries_repo = QueriesRepository()
        customers = queries_repo.query9()
        response = {
            'customers': customers
        }
        return Response(response)
