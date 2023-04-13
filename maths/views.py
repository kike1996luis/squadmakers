from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from drf_yasg import openapi
from math import lcm
from rest_framework.views import APIView

class LcmMathsAPI(APIView):
    param = openapi.Parameter('numbers', openapi.IN_QUERY,
                             description="Arreglo al cual se le hará el cálculo",
                             type=openapi.TYPE_ARRAY,
                             items=openapi.Items(type=openapi.TYPE_NUMBER))

    #Method to obtain the lcm from array
    def _lcm(self, data):
        new_array = [int(number) for number in data.split(',')]
        return lcm(*new_array)

    @swagger_auto_schema(
        operation_description="Endpoint al que se le pasa un query param llamado “numbers” con una lista de números enteros. La respuesta de este endpoint es el mínimo común múltiplo de ellos",
        manual_parameters=[param]
    )
    def get(self, request):
        if "numbers" in self.request.GET:
            lcm = self._lcm(self.request.GET.get('numbers'))
            return Response(
                {
                    "lcm": lcm,
                    "success": True
                }
            )
        return Response(
            {
                "success": False, 
                "message": "Param not found!"
            }, status=status.HTTP_404_NOT_FOUND
        )
    
class PlusMathsAPI(APIView):
    param1 = openapi.Parameter('number', openapi.IN_QUERY,
                             description="Número al cual se le hará el calculo",
                             type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        operation_description="Endpoint al que se le pasa un query param llamado “number” con un número entero. La respuesta es ese número + 1",
        manual_parameters=[param1]
    )
    def get(self, request):
        if "number" in self.request.GET:
            number = int(self.request.GET.get('number'))+1
            return Response(
                {
                    "number": number,
                    "success": True
                }
            )
        return Response(
            {
                "success": False, 
                "message": "Param not found!"
            }, status=status.HTTP_404_NOT_FOUND
        )