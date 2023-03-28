from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query22(APIView):
    def get(self, request):
        price = request.data.get('price', '0')
        queries_repo = QueriesRepository()
        items = queries_repo.query22(int(price))
        response = {
            'items': items
        }
        return Response(response)
