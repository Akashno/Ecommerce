from django.urls import path

from administrator.views import *

urlpatterns =[
    path('', admin_page, name='admin_page'),
    path('admin_approval/<int:pk>', admin_approval, name='admin_approval'),
]