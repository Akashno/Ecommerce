from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from administrator.decorators import admin_view
from administrator.models import Messages
from user.models import Order, Notification


@login_required(login_url='login_page')
@admin_view
def admin_page(request):
    messages_all = Messages.objects.all()
    orders = Order.objects.filter(delivered=False)
    context = {'orders': orders,'messages_all':messages_all}
    return render(request, 'administrator/admin_page.html', context)

@login_required(login_url='login_page')
@admin_view
def admin_approval(request, pk):
    if request.method == "POST":
        if 'deliver_order' in request.POST:
            order = Order.objects.get(id=pk)
            print(order.user)
            order.delivered = True
            order.save()
            messages.success(request, "order delivered")
            new = Notification(user=order.user,text=str(order.product.name),success=True,seen=False )
            new.save()
            return redirect('admin_page')
        elif 'cancel_order' in request.POST:
            order = Order.objects.get(id=pk)
            new = Notification(user=order.user,text=str(order.product.name),success=False,seen=False)
            new.save()
            order.delete()
            messages.success(request, "order canceled")
            return redirect('admin_page')