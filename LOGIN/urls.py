from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('authenticate/',views.login_page,name='authenticate'),
    path('logout/', views.logout_view,name='logout'),
]
