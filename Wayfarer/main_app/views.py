from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post , City
from .forms import ProfileForm , PostForm , CityForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):#also known as profile index
    current_user = request.user
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(profile=profile)
    context = {'profile': profile, 'posts':posts, 'current_user': current_user}
    return render(request,'profile/index.html', context)


@login_required
def edit_profile(request,profile_id):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            updated_profile = form.save()
            return redirect('profile')
            
    else:
        form = ProfileForm(instance=profile)
        context = {
        'profile': profile,
        'form': form
        }
        return render(request,'profile/edit.html',context)

@login_required
def city_index(request):
    all_cities = City.objects.all()
    form = CityForm()
    context = {
        'form' : form,
        'cities': all_cities
    }
    return render(request,'cities/index.html',context)

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = post.profile.id
    author = Profile.objects.get(id=profile)
    # city= post.city
    current_user = request.user
    context = {'post':post, 'author': author, 'modifiable':(current_user == author.user) }
    return render(request,'posts/detail.html', context)

@login_required
def add_post(request):
    error_message = ''
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        print(post_form.errors)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.profile = Profile.objects.get(user = request.user)
            new_post.save()
            return redirect('profile')
        else:
            error_message = post_form.errors
    context = {"post_form": PostForm(), 'error_message': error_message}
    return render(request, "posts/new.html", context)

def post_index(request, post_id):
    pass


@login_required
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    print(f'Profile: {post.profile.user}')
    if(post.profile.user != request.user):
        return render(request,'404.html')
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if  post_form.is_valid():
            updated_post = post_form.save()
            return redirect('post_detail', updated_post.id)
    else:
        form = PostForm(instance=post)
        context = { 'form': form, 'post': post }
        return render(request, 'posts/edit.html', context)


@login_required
def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('profile')



@login_required
def city_detail(request, city_id):
    posts = Post.objects.filter(city=city_id)
    city = City.objects.get(id= city_id)
    print(len(posts))
    context = {'city':city, 'posts': posts}
    return render(request,'cities/detail.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST.get('current_city'))
        if form.is_valid():
            user = form.save()
            login(request,user)
            city_choice = request.POST.get("current_city")
            matched_city = City.objects.get(id = city_choice)
            new_profile = Profile(name = request.POST.get('name'), user = user, current_city = matched_city)
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


@login_required
def add_post_inside_city(request, city_id):
    error_message = ''
    city = City.objects.get(id=city_id)
    hideCity = True
    context = {"post_form":PostForm(initial={'city': city}), 'error_message':error_message, 'city':city}
    print("HIHIIIIIT")
    return render(request,"posts/new.html",context)
