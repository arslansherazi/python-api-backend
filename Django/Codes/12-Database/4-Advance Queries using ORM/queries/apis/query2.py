from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query2(APIView):
    def get(self, request):
        cnic_no = request.data.get('cnic_no', 0)
        queries_repo = QueriesRepository()
        customer = queries_repo.query2(cnic_no)
        response = {
            'customer': customer
        }
        return Response(response)
