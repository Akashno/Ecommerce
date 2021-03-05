from django.shortcuts import redirect


def unauthenticated_view(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:

                return redirect('admin_page')
            else:
                return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func