from django.contrib import admin
from .models import *
from config.admin import custom_admin_site
# from django import forms
# Register your models here.
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','gender')
    search_fields = ('first_name','last_name','gender')
    list_filter = ('last_name','gender')
    list_per_page = 10
    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Đảm bảo bạn tạo file custom_admin.css trong thư mục static
        },
        js = ('js/admin/admin.js',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ref_no', 'user', 'flight', 'seat_class', 'status', 'total_fare', 'booking_date')  # Cột hiển thị
    list_editable = ('seat_class', 'status')  # Cho phép chỉnh sửa các trường này trực tiếp trong danh sách
    search_fields = ('ref_no', 'user__username', 'flight__origin__city', 'flight__destination__city')  # Tìm kiếm theo số tham chiếu, người dùng, và chuyến bay
    list_filter = ('status', 'seat_class', 'flight__origin', 'flight__destination')  # Bộ lọc theo trạng thái, hạng ghế, và chuyến bay
    list_editable = ('seat_class','status')
    filter_horizontal = ('passengers',)
    list_per_page = 10
    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Đảm bảo bạn tạo file custom_admin.css trong thư mục static
        },
        js = ('js/admin/admin.js',)


# Tùy chỉnh giao diện quản trị cho Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('fare', 'status', 'card_number', 'card_holder_name', 'expMonth', 'expYear', 'status')  # Cột hiển thị
    list_filter = ('status',)  # Bộ lọc theo trạng thái thanh toán và chuyến bay
    list_per_page = 10
    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Đảm bảo bạn tạo file custom_admin.css trong thư mục static
        },
        js = ('js/admin/admin.js',)

custom_admin_site.register(Payment, PaymentAdmin)
custom_admin_site.register(Ticket, TicketAdmin)
custom_admin_site.register(Passenger,PassengerAdmin)
