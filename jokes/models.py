from django.db import models

class Joke(models.Model):
    objects = models.Manager
    joke = models.TextField(max_length=255)
    
    def __str__(self):
        return f'Joke ({ self.pk}): { self.chiste }'