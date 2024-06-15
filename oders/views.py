from django.shortcuts import render,redirect
from .models import Orders
from products.models import Product

# Create your views here.

   


def view_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_ob=Orders.objects.filter(owner=customer, order_status=Orders.CART_STAGE)
    context={'cart':cart_ob}
    

    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        product_obj=Product.objects.get(pk=product_id)
        Orders.objects.create(owner=customer,product=product_obj,quantity=quantity)
    return redirect('cart_view')  