from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query11(APIView):
    def get(self, request):
        price1 = request.data.get('price1', 0)
        price2 = request.data.get('price2', 0)
        queries_repo = QueriesRepository()
        items = queries_repo.query11(price1, price2)
        response = {
            'items': items
        }
        return Response(response)
