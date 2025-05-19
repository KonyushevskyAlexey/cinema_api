import os
import django
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_api.settings')
django.setup()

from movies.models import Genre, Movie
from halls.models import Hall
from screenings.models import Screening
from tickets.models import Ticket
from users.models import User

def create_test_data():
    # Создание жанров
    genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']
    genre_objects = []
    for genre in genres:
        g, created = Genre.objects.get_or_create(name=genre)
        genre_objects.append(g)
    
    # Создание фильмов
    movies = [
        {'title': 'The Matrix', 'duration': timedelta(hours=2, minutes=16), 'genres': [genre_objects[0], genre_objects[4]]},
        {'title': 'Inception', 'duration': timedelta(hours=2, minutes=28), 'genres': [genre_objects[0], genre_objects[4]]},
        {'title': 'The Hangover', 'duration': timedelta(hours=1, minutes=40), 'genres': [genre_objects[1]]},
    ]
    
    for movie_data in movies:
        genres = movie_data.pop('genres')
        movie = Movie.objects.create(
            title=movie_data['title'],
            description=f"Description for {movie_data['title']}",
            duration=movie_data['duration'],
            release_date=timezone.now().date() - timedelta(days=365),
            director="Some Director",
            rating=8.5
        )
        movie.genres.set(genres)
    
    # Создание залов
    halls = [
        {'name': 'Hall 1', 'capacity': 100},
        {'name': 'Hall 2', 'capacity': 150},
        {'name': 'VIP Hall', 'capacity': 30},
    ]
    
    for hall_data in halls:
        Hall.objects.create(
            name=hall_data['name'],
            capacity=hall_data['capacity'],
            description=f"Description for {hall_data['name']}"
        )
    
    # Создание сеансов
    movies = Movie.objects.all()
    halls = Hall.objects.all()
    now = timezone.now()
    
    for i in range(5):
        Screening.objects.create(
            movie=movies[i % len(movies)],
            hall=halls[i % len(halls)],
            start_time=now + timedelta(days=i, hours=18),
            price=300 + i*50
        )
    
    # Создание пользователей
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123',
        role='admin'
    )
    
    User.objects.create_user(
        username='cashier',
        email='cashier@example.com',
        password='cashier123',
        role='cashier'
    )
    
    User.objects.create_user(
        username='visitor',
        email='visitor@example.com',
        password='visitor123',
        role='visitor'
    )
    
    print("Test data created successfully!")

if __name__ == '__main__':
    create_test_data()
