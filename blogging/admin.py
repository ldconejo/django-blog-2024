from django.contrib import admin

from blogging.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
