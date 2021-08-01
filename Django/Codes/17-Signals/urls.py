from django.urls import path

from apis.order.api import OrderApi
from apis.delete_order.api import DeleteOrder

urlpatterns = [
    path('order', OrderApi.as_view()),
    path('delete_order', DeleteOrder.as_view())
]
