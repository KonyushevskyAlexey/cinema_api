from rest_framework import serializers
from .models import Ticket
from screenings.models import Screening  # Добавьте этот импорт
from screenings.serializers import ScreeningSerializer

class TicketSerializer(serializers.ModelSerializer):
    screening = ScreeningSerializer(read_only=True)
    screening_id = serializers.PrimaryKeyRelatedField(
        queryset=Screening.objects.all(),  # Теперь Screening определен
        source='screening',
        write_only=True
    )
    
    class Meta:
        model = Ticket
        fields = [
            'id',
            'screening',
            'screening_id',
            'seat_number',
            'customer_name',
            'purchase_time',
            'is_booked',
            'is_paid'
        ]
