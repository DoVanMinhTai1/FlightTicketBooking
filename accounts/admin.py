from django.contrib import admin
from django.contrib.auth.models import User
from config.admin import custom_admin_site
# Register your models here.

custom_admin_site.register(User)


