# signup/views.py
from django.shortcuts import render, redirect
from .models import SIGNUP

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login, get_user_model


from django.shortcuts import render
from .models import SIGNUP


from django.shortcuts import render,redirect
 
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login 

def signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do whatever you want
            return redirect('authenticate')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})





def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            user = form.get_user()
            login(request, user)
        
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'authenticate.html', {'form': form})


@login_required(login_url='authenticate')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('signup')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)




@login_required(login_url='signup')
def home(request):
    return render(request,'home.html')
 