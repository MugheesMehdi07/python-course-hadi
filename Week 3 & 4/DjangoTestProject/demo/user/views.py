from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse

def my_view(request):
    return HttpResponse('Hello, World!')


class MyAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})

