from django.db import models
from pip._vendor.rich.status import Status

# Create your models here.
from booking.models import Booking

class Payment(models.Model):
    STATUS = (
        (0, "paid"),
        (1, "pending"),
        (2, "failed"),
    )

    receipt = models.IntegerField(null=True)
    amount_credited = models.DecimalField(decimal_places=2, max_digits=18)
    customer_name = models.CharField(max_length=250, null=True)
    customer_number = models.CharField(max_length=250, null=True)
    payment_status = models.CharField(
        max_length=200, null=True, choices=STATUS, default="pending"
    )
    paystack_payment_reference = models.CharField(
        max_length=100, default="", blank=True
    )

    def __str__(self):
        return f"{self.paystack_payment_reference}"

class Payment1(models.Model):
    STATUS = (
        (0, "paid"),
        (1, "pending"),
        (2, "failed"),
    )
    fare = models.DecimalField(decimal_places=2, max_digits=18)
    card_number = models.CharField(max_length=20, null=True)
    card_holder_name = models.CharField(max_length=150, null=True)
    expMonth = models.IntegerField(null=True)
    expYear = models.IntegerField(null=True)
    cvv =  models.IntegerField(null=True)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE,null=True)
    status = models.CharField(default=STATUS[0][1],max_length=20, null=True)
