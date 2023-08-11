from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,Http404
from django.http import JsonResponse
from base.models import Products
from .forms import ProductsForm






def products_home_view(request):
    if request.user.is_authenticated:
      context = {
         'isim':'Barış'
      }
    else :
       context = {
          'isim' : 'Misafir'
       }  
    return render(request,'home.html',context)

def products_index_view(request):
    products = Products.objects.all()
    
    return render(request, 'products/index.html',{'products':products})

    
def products_detail_view(request,id):
    product = get_object_or_404(Products,id=id)

    context = {
       'product':product
    }

    return render(request,'products/detail.html',context)

def products_create_view(request):
    if not request.user.is_authenticated:
        return Http404()


 
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/products/index')
    else:
        form = ProductsForm()
        context = {
            'form': form
        }
    
        
    return render(request,'products/form.html',context)    


def products_update_view(request,id):
    if not request.user.is_authenticated:
        return Http404()
    product = get_object_or_404(Products,id=id)
    form = ProductsForm(request.POST or None , instance = product)
    s_id = str(id)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/products/detail/' + s_id)
    else:
        context = {
            'form': form
        }
    
    return render(request,'products/form.html',context )


def products_delete_view(request,id):
    if not request.user.is_authenticated:
        return Http404()
    product = get_object_or_404(Products,id=id)
   
    form = ProductsForm(request.POST or None ,instance = product)
    if form.is_valid():
        product.delete()
        return redirect('http://127.0.0.1:8000/products/index')
    else:
        
        context = {
            'form': form
        }
    
    return render(request,'products/deleteform.html' , context)