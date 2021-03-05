from django.contrib import admin

# Register your models here.
from user.models import Order, Notification

admin.site.register(Order)
admin.site.register(Notification)