from django.urls import path	
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('newproducts', views.newproducts, name='newproducts')
]