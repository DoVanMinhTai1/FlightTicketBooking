from rest_framework import serializers
from payment.models import Payment
from booking.models import Booking
class AcceptFundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        


