from rest_framework import viewsets, filters
from .models import Screening
from .serializers import ScreeningSerializer
from .permissions import IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime

class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie', 'hall']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.query_params.get('date', None)
        if date:
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d').date()
                queryset = queryset.filter(start_time__date=date_obj)
            except ValueError:
                pass
        return queryset
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
