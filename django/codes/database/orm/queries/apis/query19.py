from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query19(APIView):
    def get(self, request):
        category = request.data.get('category', '')
        queries_repo = QueriesRepository()
        items = queries_repo.query19(category)
        response = {
            'items': items
        }
        return Response(response)
