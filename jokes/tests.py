
from django.test import TestCase
from jokes.models import Joke
from rest_framework.test import APIRequestFactory
from django.test import TransactionTestCase

import json

from jokes.models import Joke
from rest_framework.test import APIClient
from rest_framework import status

class JokesTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.client = APIClient()

    #Prueba el endpoint para agregar un nuevo chiste a la base de datos
    def test_post_joke(self):
        complete_url = '{}?{}'.format(
            '/api/jokes/add',
            '&'.join([
                'text=New Joke Added'
            ]))
        response = self.client.post(complete_url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Joke.objects.all().count(), 1, "Verifica si el elemento fue agregado")
    
    #prueba el endpoint para actualizar chiste almacenado en base de datos
    def test_update_joke(self):
        joke = Joke.objects.create(joke='Test Joke')
        joke.save()
        joke = Joke.objects.create(joke='New Test Joke')
        joke.save()
        complete_url = '{}?{}'.format(
            '/api/jokes/',
            '&'.join([
                'joke=New Joke Updated',
                'number=1'
            ]))
        response = self.client.put(
            complete_url
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Lanza respuesta 200 si el chiste fue actualizado")
        self.assertEqual(Joke.objects.filter(joke='New Joke Updated').count(), 1, "Verifica si el elemento fue modificado")

    #prueba el endpoint para borrar chiste almacenado en base de datos
    def test_delete_joke(self):
        joke = Joke.objects.create(joke='Test Joke')
        joke.save()
        joke = Joke.objects.create(joke='New Test Joke')
        joke.save()
        complete_url = '{}?{}'.format(
            '/api/jokes/',
            '&'.join([
                'number=1'
            ]))
        response = self.client.delete(complete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Debe lanzar 200 si el chiste fue eliminado")
        complete_url = '{}?{}'.format(
            '/api/jokes/',
            '&'.join([
                'number=2'
            ]))
        response = self.client.delete(complete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Debe lanzar 200 si el chiste fue eliminado")
        self.assertEqual(Joke.objects.all().count(), 0, "Verifica si no hay elementos en la base de datos debido a que fueron borrados")

    #prueba el endpoint para obtener chiste aleatorio Chuck o Dad
    def test_random_joke(self):
        
        option = 'Chuck'
        response = self.client.get(f'/api/jokes/{option}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Debe mostrar un chiste de Chuck")

        option = 'Dad'
        response = self.client.get(f'/api/jokes/{option}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Debe mostrar un chiste de Dad")

        option = 'Dads'
        response = self.client.get(f'/api/jokes/{option}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, "Debe mostrar un 404 ya que la opción no existe")
        
    #Prueba el endpoint para obtener la lista de chistes almacenada en base de datos
    def test_list_jokes(self):
        joke = Joke.objects.create(joke='Test Joke')
        joke.save()
        joke = Joke.objects.create(joke='New Test Joke')
        joke.save()
        response = self.client.get(
            '/api/jokes/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Lanza 200 si la petición fue efectuada")
        self.assertEqual(2, len(response.data['jokes']), "Comprueba si hay dos chistes nuevos almacenados")