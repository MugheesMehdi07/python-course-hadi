from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy

urlpatterns = [
    # path('', MyAPIView.as_view()),
    path('users/', UserListCreate.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view()),


]





