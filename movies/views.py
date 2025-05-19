from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdmin

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genres']
    search_fields = ['title', 'director']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
