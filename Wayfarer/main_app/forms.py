from django import forms
from .models import Profile , Post

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name',)

class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ("title","content","date","image")
