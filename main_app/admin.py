from django.contrib import admin
from .models import Profile, City, Post, Comment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(City)
admin.site.register(Comment)
