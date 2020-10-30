from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length = 100)
    current_city = models.ForeignKey(City, on_delete = models.CASCADE)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 250)
    content = models.TextField(max_length = 1000)
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
