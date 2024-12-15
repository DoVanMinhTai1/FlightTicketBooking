from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Trang chủ
    path('contact', views.contact, name="contact"),
    path('privacy-policy', views.privacy_policy, name="privacypolicy"),
    path('terms-and-conditions', views.terms_and_conditions, name="termsandconditions"),
    path('about-us', views.about_us, name="aboutus"),
]