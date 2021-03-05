from django.urls import path

from user.views import *

urlpatterns = [
    path('', index, name='index'),
    path('explore/', explore, name='explore'),
    path('mens/', mens, name='mens'),
    path('womens/', womens, name='womens'),
    path('kids/', kids, name='kids'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:pk>/<str:backto>', add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:pk>', delete_from_cart, name='delete_from_cart'),
    path('empty_cart/', empty_cart, name='empty_cart'),
    path('place_order/', place_order, name='place_order'),
    path('delete_order/<int:pk>', delete_order, name='delete_order'),
    path('notification/', notification, name='notification'),
    path('seen/<int:pk>', seen, name='seen'),
    path('profile/', profile, name='profile'),
]