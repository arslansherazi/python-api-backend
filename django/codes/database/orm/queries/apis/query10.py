from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query10(APIView):
    def get(self, request):
        records_limit = request.data.get('records_limit', '0')
        queries_repo = QueriesRepository()
        items = queries_repo.query10(int(records_limit))
        response = {
            'items': items
        }
        return Response(response)
