from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def edit_profile(request,profile_id):
    pass

def about(request):
    return render(request, 'about.html')

def profile(request):
    pass


def post_index(request, post_id):
    pass
