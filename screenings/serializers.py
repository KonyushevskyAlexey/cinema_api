from rest_framework import serializers
from .models import Screening  # Импорт модели Screening
from movies.models import Movie
from halls.models import Hall
from movies.serializers import MovieSerializer
from halls.serializers import HallSerializer

class ScreeningSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source='movie',
        write_only=True
    )
    hall = HallSerializer(read_only=True)
    hall_id = serializers.PrimaryKeyRelatedField(
        queryset=Hall.objects.all(),
        source='hall',
        write_only=True
    )
    
    class Meta:
        model = Screening  # Исправлено с screening на Screening
        fields = [
            'id',
            'movie',
            'movie_id',
            'hall',
            'hall_id',
            'start_time',
            'end_time',
            'price'
        ]
