from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from payment.models import Payment1
from frontend.template import *
def payment_view(request):
    if request.method == "POST":
        # lấy dữ liệu trên form
        fare = request.POST.get("fare")
        cardNumber = request.POST.get('cardNumber')
        cardHolderName = request.POST.get('cardHolderName')
        expMonth = int(request.POST.get('expMonth'))
        expYear = int(request.POST.get('expYear'))
        cvv = request.POST.get('cvv')

        # Kiểm tra số của thẻ có dưới 16 chữ số hay không. Không thì báo lỗi
        if len(cardNumber) < 16:
            messages.warning(request,'Card number must be at least 16 digits')
            return render(request, 'payment.html')

        # Lấy ngày tháng năm hiện tại.
        current_year = datetime.today().year
        current_month = datetime.today().month
        # Kiểm tra xem thời gian hiệu lực của thẻ
        if expYear < current_year or (expYear == current_year and expMonth < current_month):
            messages.warning(request, 'Card expired')
            return render(request, 'payment.html')

        # Nếu thẻ còn hạn thì tạo thanh toán
        payment = Payment1.objects.create(
            fare = fare,
            card_number = cardNumber,
            card_holder_name = cardHolderName,
            expMonth = expMonth,
            expYear = expYear,
            cvv = cvv,
        )
        payment.save()

        # Chuyển hướng đến trang thông báo thanh toán
        return redirect('process')
    return render(request, 'payment.html')

def payment_process(request):
    return render(request, 'payment_process.html')
