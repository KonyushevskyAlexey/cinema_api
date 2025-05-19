from django.db import models

from screenings.models import Screening
from django.contrib.auth import get_user_model

User = get_user_model()

class Ticket(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=255)
    purchase_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_booked = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Ticket {self.id} for {self.screening.movie.title}"
