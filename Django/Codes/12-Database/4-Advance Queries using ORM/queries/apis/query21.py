from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query21(APIView):
    def get(self, request):
        items_count = request.data.get('items_count', '0')
        queries_repo = QueriesRepository()
        items_count = queries_repo.query21(int(items_count))
        response = {
            'items_count': items_count
        }
        return Response(response)
