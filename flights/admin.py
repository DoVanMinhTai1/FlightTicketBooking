# flights/admin.py
from django.contrib import admin
from .models import Place, Week, Flight
from config.admin import custom_admin_site

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('city', 'airport', 'code', 'country')  # Hiển thị các trường trong danh sách
    search_fields = ('city', 'country')  # Thêm khả năng tìm kiếm theo city và country
    list_filter = ('country',)  # Lọc theo quốc gia
    list_per_page = 10
    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Đảm bảo bạn tạo file custom_admin.css trong thư mục static
        },
        js = ('js/admin/admin.js',)

class WeekAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')  # Hiển thị số tuần và tên
    list_filter = ('name',)  # Lọc theo tên tuần
    list_per_page = 10
    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Đảm bảo bạn tạo file custom_admin.css trong thư mục static
        },
        js = ('js/admin/admin.js',)

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'depart_time', 'arrival_time', 'airline', 'economy_fare','business_fare','first_fare')  # Hiển thị các trường quan trọng
    search_fields = ('id','origin__city', 'destination__city', 'airline','economy_fare')  # Tìm kiếm theo tên sân bay và hãng hàng không
    list_filter = ('airline', 'origin__country')  # Lọc theo hãng hàng không và quốc gia  
    # , 'destination__country'
    # Thêm khả năng chỉnh sửa các trường quan trọng ngay trên danh sách
    list_editable = ('economy_fare', 'business_fare', 'first_fare') 
    list_per_page = 10
    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Đảm bảo bạn tạo file custom_admin.css trong thư mục static
        },
        js = ('js/admin/admin.js',)

custom_admin_site.register(Place, PlaceAdmin)
custom_admin_site.register(Week, WeekAdmin)
custom_admin_site.register(Flight, FlightAdmin)
