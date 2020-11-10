from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
	products = Product.objects.all()
	return render(request, 'index.html', {'products' : products})
	

def newproducts(request):
	return HttpResponse('Hello, these are the new products for your perusing pleasure.')
	