from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query5(APIView):
    def get(self, request):
        category1 = request.data.get('category1', '')
        category2 = request.data.get('category2', '')
        queries_repo = QueriesRepository()
        items = queries_repo.query5(category1, category2)
        items_names = []
        for item in items:
            item_name = item.get('name', '')
            items_names.append(item_name)
        response = {
            'items_names': items_names
        }
        return Response(response)
