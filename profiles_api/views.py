from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   #list of handy http status code, we will use it in our post function handler
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """
    Test API View method
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a list of APIview features
        """
        an_apiview = [
            'Use HTTP Methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'It mapped manually to URLs',
        ]

        return Response( {
        'message' : 'Hello',
        'an_apiview' : an_apiview
        } )

    def post(self, request):
        """
        Create hello message with our name
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message' : message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Use to update object, we make a request and it will update the object
        """
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """
        Handle partial update, such as only last name and first name
        """
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """
        Delete object
        """
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
