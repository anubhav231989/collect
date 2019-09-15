from rest_framework import serializers
from .models import Movie, Actor, Cast

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("created", "title", "genre", "watched",)

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("name", "gender",)


