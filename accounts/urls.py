from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('contact-us/', views.contactus, name="contactus"),
    path('about-us/', views.aboutus, name="aboutus"),
    path('home/',views.home,name='home'),
    path('laptop-price/',views.laptopprice,name='laptopprice'),
]