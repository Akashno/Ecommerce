from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect

from administrator.models import Product, Messages
from user.decorators import user_view
from user.models import Cart, Order, Notification


@user_view
def index(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        object = Messages(name=name, email=email, message=message)
        object.save()
        messages.success(request, 'message sent successfully')
        return redirect('index')
    cart_count = ""
    noti_count = ""
    if not request.user.is_anonymous:
        cart_count = Cart.objects.filter(user=request.user).count()
        noti_count = Notification.objects.filter(user=request.user, seen=False).count()
        if cart_count <= 0:
            cart_count = ""
        if noti_count <= 0:
            noti_count = ""
    products = Product.objects.all()
    context = {'cart_count': cart_count, 'noti_count': noti_count,'products':products}
    return render(request, 'user/index.html', context)


@user_view
def explore(request):
    cart_count = ""
    noti_count = ""
    if not request.user.is_anonymous:
        cart_count = Cart.objects.filter(user=request.user).count()
        noti_count = Notification.objects.filter(user=request.user, seen=False).count()
        if cart_count <= 0:
            cart_count = ""
        if noti_count <= 0:
            noti_count = ""
    products = Product.objects.all()
    context = {'products': products, 'cart_count': cart_count, 'noti_count': noti_count}
    return render(request, 'user/explore.html', context)


@user_view
def mens(request):
    products = Product.objects.filter(catogory='mens')
    cart_count = ""
    noti_count = ""
    if not request.user.is_anonymous:
        cart_count = Cart.objects.filter(user=request.user).count()
        noti_count = Notification.objects.filter(user=request.user, seen=False).count()
        if cart_count <= 0:
            cart_count = ""
        if noti_count <= 0:
            noti_count = ""
    context = {'products': products, 'cart_count': cart_count, 'noti_count': noti_count}
    return render(request, 'user/mens.html', context)


@user_view
def womens(request):
    products = Product.objects.filter(catogory='womens')
    cart_count = ""
    noti_count = ""
    if not request.user.is_anonymous:
        cart_count = Cart.objects.filter(user=request.user).count()
        noti_count = Notification.objects.filter(user=request.user, seen=False).count()
        if cart_count <= 0:
            cart_count = ""
        if noti_count <= 0:
            noti_count = ""
    context = {'products': products, 'cart_count': cart_count, 'noti_count': noti_count}
    return render(request, 'user/womens.html', context)


@user_view
def kids(request):
    products = Product.objects.filter(catogory='kids')
    cart_count = ""
    noti_count = ""
    if not request.user.is_anonymous:
        cart_count = Cart.objects.filter(user=request.user).count()
        noti_count = Notification.objects.filter(user=request.user, seen=False).count()
        if cart_count <= 0:
            cart_count = ""
        if noti_count <= 0:
            noti_count = ""
    context = {'products': products, 'cart_count': cart_count, 'noti_count': noti_count}
    return render(request, 'user/kids.html', context)


@user_view
def cart(request):
    product_count = Cart.objects.aggregate(Sum('count'))
    product_total = Cart.objects.aggregate(Sum('total'))
    items = Cart.objects.all()
    cart_count = ""
    noti_count = ""
    if not request.user.is_anonymous:
        cart_count = Cart.objects.filter(user=request.user).count()
        noti_count = Notification.objects.filter(user=request.user, seen=False).count()
        if cart_count <= 0:
            cart_count = ""
        if noti_count <= 0:
            noti_count = ""
    context = {'items': items, 'cart_count': cart_count, 'noti_count': noti_count,
               'pc': product_count['count__sum'],
               'pt': product_total['total__sum']}
    return render(request, 'user/cart.html', context)


@user_view
def add_to_cart(request, pk, backto):
    product = Product.objects.get(id=pk)
    if Cart.objects.filter(product=product).exists():
        cart_item = Cart.objects.get(product=product)
        cart_item.update_count()
        cart_item.get_total()
        cart_item.save()
        return redirect(backto)
    else:
        cart_item = Cart(user=request.user, product=product)
        cart_item.get_total()
        cart_item.save()
        return redirect(backto)


@user_view
def delete_from_cart(request, pk):
    item = Cart.objects.get(id=pk)
    item.delete()
    messages.success(request, 'Item deleted from cart')
    return redirect('cart')


@user_view
def empty_cart(request):
    cart = Cart.objects.filter(user=request.user)
    cart.delete()
    return redirect('cart')


@user_view
def place_order(request):
    items = Cart.objects.filter(user=request.user)
    for item in items:
        order = Order(user=item.user, product=item.product, count=item.count, total=item.total)
        order.save()
    messages.success(request, "New Orders Placed Successfully")
    Cart.objects.all().delete()
    return redirect('profile')


@user_view
def profile(request):
    items = Order.objects.filter(user=request.user)
    context = {'items': items}
    return render(request, 'user/profile.html', context)


@user_view
def delete_order(request, pk):
    item = Order.objects.filter(id=pk, user=request.user)
    item.delete()
    messages.success(request, 'Order deleted successfully')
    return redirect('profile')


@user_view
def notification(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-id')
    delete_notifications(request)
    context = {'notifications': notifications}
    return render(request, 'user/notification.html', context)


@user_view
def seen(request, pk):
    item = Notification.objects.get(user=request.user, id=pk)
    item.seen = True
    item.save()

    return redirect('notification')


#################################################################tweeks
def delete_notifications(request):
    from django.utils import timezone
    today = timezone.now()
    notifications = Notification.objects.filter(user=request.user, seen=True)
    for n in notifications:
        if today > n.date_created + timezone.timedelta(days=30):
            n.delete()
