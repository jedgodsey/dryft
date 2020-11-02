from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def edit_profile(request,profile_id):
    pass

def about(request):
    pass

def profile(request):
    return render(request, 'profile.html')


def post_index(request, post_id):
    pass