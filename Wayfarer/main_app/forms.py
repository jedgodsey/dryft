from django import forms
from .models import Profile , Post , City

class ProfileForm(forms.ModelForm):
    current_city = forms.ModelChoiceField(queryset=City.objects.all())
    class Meta:      
        model = Profile
        fields = ("name", "email", "profile_picture", "current_city")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","content","date","city","image",)

class CityForm(forms.ModelForm):
    # cities = forms.ModelChoiceField(queryset=City.objects.all())
    class Meta:
        model = City
        fields = ("name","country")
