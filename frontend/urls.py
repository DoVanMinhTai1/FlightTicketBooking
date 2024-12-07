from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Trang chủ
    path('about/', views.about, name='about'),  # Trang About
  
]