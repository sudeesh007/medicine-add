from . import views
from django.urls import path

urlpatterns = [
        path('create/',views.product_create,name='createproduct'),
        path('listing/',views.listing,name='page_list'),
        path('retrieve/',views.product_read,name='retrieveproduct'),
        path('update/<int:id>/',views.product_update,name='updateproduct'),
         path('delete/<int:pk>',views.product_delete,name='deleteproduct'),
       
         path('search/', views.search_view, name='search'),
         path('search/products/', views.search_products, name='search_products'),
          path('mproducts/delete/<int:pk>/', views.product_delete, name='product_delete'),
         
    ]