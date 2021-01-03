from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext as _
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='images/city_pics/', null=True)
    image_url = models.URLField(null=True, max_length = 500)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200, null=True)
    current_city = models.ForeignKey(City, on_delete = models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='images/profile_pics/', default='images/profile_pics/place_holder.jpg' , null = True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 1000)
    date = models.DateField(_("Date"), default=datetime.date.today)
    image = models.ImageField(upload_to='images/post_pics/', null = True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    city = models.ForeignKey(City, on_delete = models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 500)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)


    def __str__(self):
        return self.comment


# delete this comment
