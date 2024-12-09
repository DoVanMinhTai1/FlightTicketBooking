from django.urls import path
from payment import views

urlpatterns = [
    path("checkout/",views.payment_view,name="checkout")
]