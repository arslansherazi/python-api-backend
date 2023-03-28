from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query26(APIView):
    def get(self, request):
        queries_repo = QueriesRepository()
        items = queries_repo.query26()
        response = {
            'items': items
        }
        return Response(response)
