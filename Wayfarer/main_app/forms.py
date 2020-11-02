from django import forms
from .models import Profile , Post

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name','profile_picture')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","content","date","city","image",)
