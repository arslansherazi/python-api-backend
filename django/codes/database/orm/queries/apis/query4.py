from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query4(APIView):
    def get(self, request):
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        queries_repo = QueriesRepository()
        customers = queries_repo.query4(first_name, last_name)
        response = {
            'customers': customers
        }
        return Response(response)
