from django.urls import path
from .views import OrderListCreate, OrderRetrieveUpdateDestroy

urlpatterns = [
    path('orders/', OrderListCreate.as_view()),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view()),
]
