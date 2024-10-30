from django.db import models
from registration.models import Registration

class Payment(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment for {self.registration.student.username} - {self.amount}'
