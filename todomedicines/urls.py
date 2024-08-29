from django.urls import path,include
from LOGIN import views

urlpatterns =  [ path('', views.signup_page, name='signup'),
                 path('home/',views.home,name='home'),
                 path('mproducts/',include('mproducts.urls')),
                 path('LOGIN/',include('LOGIN.urls')),
                 
                ]

    
    


