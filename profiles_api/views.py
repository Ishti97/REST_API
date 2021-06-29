from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of Api View Features"""

        an_apiview = {
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to django view',
            'More control',
            'Is mapped manually to URLs',
        }

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})