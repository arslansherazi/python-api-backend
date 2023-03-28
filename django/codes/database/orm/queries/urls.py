from django.urls import include, path

from queries.apis.query1 import Query1
from queries.apis.query2 import Query2
from queries.apis.query3 import Query3
from queries.apis.query4 import Query4
from queries.apis.query5 import Query5
from queries.apis.query6 import Query6
from queries.apis.query7 import Query7
from queries.apis.query8 import Query8
from queries.apis.query9 import Query9
from queries.apis.query10 import Query10
from queries.apis.query11 import Query11
from queries.apis.query12 import Query12
from queries.apis.query13 import Query13
from queries.apis.query14 import Query14
from queries.apis.query15 import Query15
from queries.apis.query16 import Query16
from queries.apis.query18 import Query18
from queries.apis.query19 import Query19
from queries.apis.query20 import Query20
from queries.apis.query21 import Query21
from queries.apis.query22 import Query22
from queries.apis.query23 import Query23
from queries.apis.query24 import Query24
from queries.apis.query25 import Query25
from queries.apis.query26 import Query26
from queries.apis.query27 import Query27
from queries.apis.query28 import Query28

urlpatterns = [
    # apis' views
    path('query1', Query1.as_view()),
    path('query2', Query2.as_view()),
    path('query3', Query3.as_view()),
    path('query4', Query4.as_view()),
    path('query5', Query5.as_view()),
    path('query6', Query6.as_view()),
    path('query7', Query7.as_view()),
    path('query8', Query8.as_view()),
    path('query9', Query9.as_view()),
    path('query10', Query10.as_view()),
    path('query11', Query11.as_view()),
    path('query12', Query12.as_view()),
    path('query13', Query13.as_view()),
    path('query14', Query14.as_view()),
    path('query15', Query15.as_view()),
    path('query16', Query16.as_view()),
    path('query18', Query18.as_view()),
    path('query19', Query19.as_view()),
    path('query20', Query20.as_view()),
    path('query21', Query21.as_view()),
    path('query22', Query22.as_view()),
    path('query23', Query23.as_view()),
    path('query24', Query24.as_view()),
    path('query25', Query25.as_view()),
    path('query26', Query26.as_view()),
    path('query27', Query27.as_view()),
    path('query28', Query28.as_view())
]