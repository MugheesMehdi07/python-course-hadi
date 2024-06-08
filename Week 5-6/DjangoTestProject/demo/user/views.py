from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse

# def my_view(request):
#     return HttpResponse('Hello, World!')
#
#
# class MyAPIView(APIView):
#     def get(self, request):
#         return Response({"user": "Mughees"})



from rest_framework import generics
from .models import UserProfile
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all() # SELECT * FROM UserProfile
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


