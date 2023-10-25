from django.contrib import admin
from app1.models import Products,Reviews,Cart

# Register your models here.

admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Reviews)
