from django.urls import path


from authenticate.views import *

urlpatterns =[
    path('register_page/', register_page, name="register_page"),
    path('login_page/', login_page, name="login_page"),
    path('logout_page/', logout_page, name='logout_page'),
]