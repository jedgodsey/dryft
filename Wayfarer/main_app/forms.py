from django import forms
from .models import Profile , Post , City , Comment

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
<<<<<<< HEAD
        fields = ("name","country","image")


class CityForm1(forms.ModelForm):
    # cities = forms.ModelChoiceField(queryset=City.objects.all())
    class Meta:
        model = City
        fields = ("name","country","image_url")       
=======
        fields = ("name","country", "image")
>>>>>>> submaster

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("comment",)
