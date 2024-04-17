from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> Response
# Request handler
# Actions
# In django its called views.

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
#pull data from db
#send emails
#transform
    #return HttpResponse('Hello World')
    x = calculate()
    return render(request, 'hello.html', {'name': 'Jackie'})