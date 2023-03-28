from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query28(APIView):
    def get(self, request):
        customer_id = request.data.get('customer_id', 0)
        category = request.data.get('category', '')
        queries_repo = QueriesRepository()
        customer_info = queries_repo.query28(int(customer_id), category)
        response = {
            'customer_info': customer_info
        }
        return Response(response)
