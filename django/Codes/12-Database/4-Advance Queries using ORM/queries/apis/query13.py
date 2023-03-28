from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query13(APIView):
    def get(self, request):
        queries_repo = QueriesRepository()
        order_details = queries_repo.query13()
        response = {
            'order_details': order_details
        }
        return Response(response)
