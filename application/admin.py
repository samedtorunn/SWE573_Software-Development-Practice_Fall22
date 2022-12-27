from django.contrib import admin
from .models import Post, UserProfile, Space, Comment

# Register your models here.


admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Space)
admin.site.register(Comment)


