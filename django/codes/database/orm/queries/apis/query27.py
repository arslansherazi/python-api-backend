from rest_framework.response import Response
from rest_framework.views import APIView

from queries.repository import QueriesRepository


class Query27(APIView):
    def get(self, request):
        queries_repo = QueriesRepository()
        names = queries_repo.query27()
        response = {
            'names': names
        }
        return Response(response)
