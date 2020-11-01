from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:post_id>', views.post_index, name='post_index'),
    path('accounts/signup', views.signup, name='signup'),
]
