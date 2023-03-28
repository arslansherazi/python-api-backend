from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query14(APIView):
    def get(self, request):
        queries_repo = QueriesRepository()
        items_orders = queries_repo.query14()
        response = {
            'items_orders': items_orders
        }
        return Response(response)
