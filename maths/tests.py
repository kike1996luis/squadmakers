
from django.test import TestCase
from jokes.models import Joke
from rest_framework.test import APIRequestFactory

import json

from jokes.models import Joke
from rest_framework.test import APIClient
from rest_framework import status

class MathTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    #Test para probar el minimo común múltiplo de un arreglo de números
    def test_lcm_math(self):
        payload = {
            'numbers': '2,5,6'
        }
        response = self.client.get(
            '/api/math/lcm/', 
            payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Muestra si la petición fue efectuada")
        self.assertEqual(30, response.data['lcm'], "Muestra si el MCM es correcto")

        payload['numbers'] ='11,17,53'
        response = self.client.get(
            '/api/math/lcm/', 
            payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Muestra si la petición fue efectuada")
        self.assertEqual(9911, response.data['lcm'], "Muestra si el MCM es correcto")

    #Test para probar el cálculo de un número + 1
    def test_plus_math(self):
        payload = {
            'number': 8
        }
        response = self.client.get(
            '/api/math/plus/',
            payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Muestra si la petición fue efectuada")
        self.assertEqual(9, response.data['number'], "Muestra si el cálculo es correcto")

        payload['number'] = 2
        response = self.client.get(
            '/api/math/plus/',
            payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Muestra si la petición fue efectuada")
        self.assertEqual(3, response.data['number'], "Muestra si el cálculo es correcto")