from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query3(APIView):
    def get(self, request):
        queries_repo = QueriesRepository()
        categories = queries_repo.query3()
        categories_data = []
        for category in categories:
            categories_data.append(category.get('category', ''))
        response = {
            'categories': categories_data
        }
        return Response(response)
