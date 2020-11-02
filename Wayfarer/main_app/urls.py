from django.contrib import admin
from django.urls import path  , include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
    path('post/new', views.add_post, name='add_post'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('city/<int:city_id>', views.city_detail, name='city_detail'),
    path('accounts/signup', views.signup, name='signup'),
]
