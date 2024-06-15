from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_products(request):
    procuct_list=Product.objects.all()
    context={'products':procuct_list}
    return render(request,'products.html',context)

def detail_products(request,pk):
    p_object=Product.objects.get(pk=pk)
    obj={
        'key':p_object
    }
    return render(request,'product_details.html',obj)