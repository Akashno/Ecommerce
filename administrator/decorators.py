from django.shortcuts import redirect


def admin_view(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func