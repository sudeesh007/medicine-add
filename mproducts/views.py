from django.shortcuts import render, redirect
from .forms import ProductForm
from django.http import HttpResponse

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Product
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product


def product_create(request):
    
    if Product.objects.count() >= 5:
        return HttpResponse("Error: Maximum number of products reached")

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form': form})





def listing(request):
    
    product_list = Product.objects.all().order_by('-added_time')

    
    paginator = Paginator(product_list, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})






def product_read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})





@login_required(login_url='signup')
def product_update(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})




@login_required(login_url='signup')
def product_delete(request, pk):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product = Product.objects.get(pk=pk)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)



@login_required(login_url='signup')
def search_view(request):
    return render(request, 'search.html')



@login_required(login_url='signup')
def search_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__istartswith=query)
        data = [{'id': product.id, 'name': product.name} for product in products]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse([], safe=False)
