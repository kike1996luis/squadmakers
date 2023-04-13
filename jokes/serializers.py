from rest_framework import serializers
from .models import Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ('id', 'joke')

    def create(self, validated_data):
        joke = Joke.objects.create(**validated_data)
        return joke