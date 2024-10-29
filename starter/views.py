from django.shortcuts import render,redirect,get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    products = Product.objects.all()  # Corrected the query to use 'objects' instead of 's'
    context = {
        'products': products
    }
    return render(request, 'starter/home.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')  
    else:
        form = ProductForm()
    
    return render(request, 'starter/create_product.html', {'form': form})

def update_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ProductForm(instance=product)
    return render(request,'starter/create_product.html',{'form':form})


def delete_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        product.delete()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'starter/delete_product.html')

        


