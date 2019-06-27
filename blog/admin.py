from django.contrib import admin

from blog.models import Post


class Post_fields(admin.ModelAdmin):
    list_display = ('created_date', 'text')
    list_filter = ['created_date']


admin.site.register(Post, Post_fields)
