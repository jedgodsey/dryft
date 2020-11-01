from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def edit_profile(request,profile_id):
    pass

def about(request):
    pass

@login_required
def profile(request):#also known as profile index
    pass


def post_index(request, post_id):
    pass

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
        else:
            error_message = 'Invalid Sign Up - try again'
    
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request,'registration/signup.html', context)