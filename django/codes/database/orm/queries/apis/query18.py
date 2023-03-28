from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query18(APIView):
    def get(self, request):
        category1 = request.data.get('category1', '')
        category2 = request.data.get('category2', '')
        queries_repo = QueriesRepository()
        items = queries_repo.query18(category1, category2)
        response = {
            'items': items
        }
        return Response(response)
