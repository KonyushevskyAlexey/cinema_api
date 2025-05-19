from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import IsAdminOrCashier, IsOwnerOrAdmin

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    
    def get_queryset(self):
        if self.request.user.is_admin():
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAdminOrCashier]
        elif self.action == 'create':
            permission_classes = [IsAdminOrCashier]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
