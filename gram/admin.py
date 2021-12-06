from gram.models import Comment, Follow, Image, Profile
from django.contrib import admin

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)