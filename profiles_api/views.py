from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """
    Test API View method
    """

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
