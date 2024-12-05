from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class InforUser(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    full_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    cccd = models.CharField(max_length=120)
    type = models.CharField(max_length=50)
    birthday = models.DateField()

