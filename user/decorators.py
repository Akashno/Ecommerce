from django.shortcuts import redirect

from user.models import Cart, Notification



def user_view(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('admin_page')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
