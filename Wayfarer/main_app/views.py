from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
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
    profile = Profile.objects.filter(user=request.user)
    return render(request,'profile/index.htmn', profile)

def post_index(request, post_id):
    pass

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST.get('name'))
        if form.is_valid():
            user = form.save()
            login(request,user)
            new_profile = Profile(name = request.POST.get('name'), user = user)
            new_profile.save()
            return redirect('profile')
        else:
            error_message = 'Invalid Sign Up - try again'
    
    form = UserCreationForm()
    profile_form  = ProfileForm()
    context = {
        'profile_form': profile_form,
        'form': form,
        'error_message': error_message
    }
    return render(request,'registration/signup.html', context)