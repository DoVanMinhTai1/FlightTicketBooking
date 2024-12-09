from django.shortcuts import render
from frontend import template
def payment_view(request):
    return render(request,'payment.html')