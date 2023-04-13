from rest_framework import generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import JokeSerializer
from .models import Joke
from drf_yasg import openapi
from rest_framework import status
from rest_framework.views import APIView
import requests

class UpdateJokesAPI(generics.ListAPIView):
    serializer_class = JokeSerializer
    queryset = Joke.objects.all()
    chuck = 'https://api.chucknorris.io/jokes/random'
    dad = 'https://icanhazdadjoke.com/'
    query_param = openapi.Parameter('joke', openapi.IN_QUERY,
                             description="Nuevo chiste para sustituir",
                             type=openapi.TYPE_STRING)
    query_param1 = openapi.Parameter('number', openapi.IN_QUERY,
                             description="Id para consulta del chiste almacenado",
                             type=openapi.TYPE_INTEGER)
    
    @swagger_auto_schema(
        operation_description="Obtener todos los chistes registrados",
    )
    def get(self, request):
        queryset = Joke.objects.all()
        serializer = JokeSerializer(queryset, many=True)
        if len(serializer.data) == 0:
            return Response(
                {
                "success": False, 
                "message": "There is no jokes registered"
                }
            )
        return Response(
            {
                "jokes": serializer.data, 
                "success": True, 
                "message": "Joke list obtained!"
            }
        )

    @swagger_auto_schema(
        operation_description="Elimina el chiste indicado en el parámetro number",
        manual_parameters=[query_param1]
    )
    def delete(self, request):
        number = self.request.GET.get('number')
        jokes = Joke.objects.filter(id=number)
        if len(jokes) == 0:
            return Response({'message': 'Joke not found', "success": False}, status=status.HTTP_404_NOT_FOUND)
        jokes.delete()
        return Response({
            "message": "Joke delete successfully!",
            "id": number,
            "success": True
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro “number”",
        manual_parameters=[query_param, query_param1]
    )
    def put(self, request):
        number = self.request.GET.get('number')
        jokes = Joke.objects.filter(id=number)
        if len(jokes) == 0:
            return Response({'message': 'Joke not found', "success": False}, status=status.HTTP_404_NOT_FOUND)
        new_joke = self.request.GET.get('joke')
        object = Joke.objects.get(id=number)
        object.joke = new_joke
        object.save()
        queryset = Joke.objects.filter(pk=number)
        serializer = JokeSerializer(queryset, many=True)
        return Response({
            "message": "Joke updated successfully",
            "joke": serializer.data,
            "success": True
        }, status=status.HTTP_200_OK)

class AddJokeAPI(generics.ListAPIView):
    serializer_class = JokeSerializer
    queryset = Joke.objects.all()
    query_param = openapi.Parameter('text', openapi.IN_QUERY,
                             description="Nuevo chiste",
                             type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        operation_description="Guarda en una base de datos el chiste el texto pasado por parámetro",
        manual_parameters=[query_param]
    )
    def post(self, request):
        serializer = self.get_serializer(data={"joke": request.query_params.get('text')})
        serializer.is_valid(raise_exception=True)
        joke = serializer.save()
        return Response({
            "joke": JokeSerializer(joke, context=self.get_serializer_context()).data,
            "message": "New joke added",
            "success": True
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(auto_schema=None)
    def get(self, request):
        pass

class RandomJokeAPI(generics.ListAPIView):
    
    serializer_class = JokeSerializer
    queryset = Joke.objects.all()
    chuck = 'https://api.chucknorris.io/jokes/random'
    dad = 'https://icanhazdadjoke.com/'

    @swagger_auto_schema(
        operation_description="Obtiene chiste aleatorio (Chuck o Dad) en path params",
    )
    def get(self, request, type: str):
        if type == 'Chuck':
            data = requests.get(url = self.chuck)
            if data.status_code != 200:
                return Response({'message': 'Request to Joke failed', "success": False}, status=status.HTTP_404_NOT_FOUND)
            return self._getJoke(data.json()['value'])
        
        elif type == 'Dad':
            data = requests.get(url = self.dad, headers = {"Accept": "application/json"})
            if data.status_code != 200:
                return Response({'message': 'Request to Joke failed', "success": False}, status=status.HTTP_404_NOT_FOUND)
            return self._getJoke(data.json()['joke'])
        return Response({'message': 'Option not found', "success": False}, status=status.HTTP_404_NOT_FOUND)
    
    # Method for response a new joke
    def _getJoke(self, joke: str):
        return Response({
            "joke": joke,
            "message": "Random joke obtained successfully",
            "success": True
        }, status=status.HTTP_200_OK)
