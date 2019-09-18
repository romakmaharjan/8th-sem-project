from django.urls import path,include
from . import views

urlpatterns = [
	path('/',views.home,name='home'),
	path('laptop-price/',views.laptopprice,name='laptopprice'),
	path('create',views.create,name='create'),
	path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
	]