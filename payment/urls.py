from django.urls import path
from payment import views

urlpatterns = [
    path('checkout/',views.payment_view,name='checkout'),
    path('book/', views.book, name='book'),
    path('checkout/api/<str:ref>', views.ticket_data, name="ticketdata"),
    path('book/<int:flight_id>/', views.book, name='book'),
]