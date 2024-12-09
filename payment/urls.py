from django.urls import path
from payment import views

urlpatterns = [
    path('checkout/',views.payment_view,name='checkout'),
    path('process/',views.payment_process,name='process'),
]