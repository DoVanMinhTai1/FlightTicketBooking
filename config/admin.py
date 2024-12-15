from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "My Custom Admin Header"
    site_title = "My Custom Admin Title"
    index_title = "Welcome to My Admin Dashboard"

custom_admin_site = CustomAdminSite(name='custom_admin')