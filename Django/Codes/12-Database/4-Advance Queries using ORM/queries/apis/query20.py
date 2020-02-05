from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query20(APIView):
    def get(self, request):
        item_id = request.data.get('item_id', '0')
        queries_repo = QueriesRepository()
        item = queries_repo.query20(int(item_id))
        response = {
            'item': item
        }
        return Response(response)
