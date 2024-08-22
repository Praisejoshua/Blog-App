from django.contrib import admin

# what i added
from trying.models import Post, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

