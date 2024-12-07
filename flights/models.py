from django.db import models
from datetime import datetime
class Place(models.Model):
    """Place model for storing origin and destination places."""
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Week(models.Model):
    """Week model for storing days of the week."""
    number = models.IntegerField(unique=True)  # Store weekday number (0-6 for Mon-Sun)
    name = models.CharField(max_length=20)     # Store the name of the day (e.g., 'Monday')

    def __str__(self):
        return self.name


class Flight(models.Model):
    """Flight model for storing flight details."""
    
    flight_name = models.CharField(max_length=150, null=False)
    origin = models.ForeignKey(Place, related_name='departure_flights', on_delete=models.CASCADE, default=None)
    destination = models.ForeignKey(Place, related_name='arrival_flights', on_delete=models.CASCADE,null=True)
    
    economy_fare = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    business_fare = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    first_fare = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    
    seats_available = models.IntegerField()
    plane_name = models.CharField(max_length=150, null=False)
    time_of_departure = models.DateTimeField()
    time_of_arrival = models.DateTimeField()
    depart_day = models.ForeignKey(Week, related_name='flights', on_delete=models.CASCADE,null=True)  # Link to Week for weekday
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.flight_name} from {self.origin} to {self.destination}"
