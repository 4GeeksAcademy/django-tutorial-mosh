from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('Hello World')
	

def newproducts(request):
	return HttpResponse('Hello, these are the new products for your perusing pleasure.')
	