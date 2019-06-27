from django.urls import path
from blog import views


app_name='blog_urls'
urlpatterns = [
    path('', views.PostIndexView, name = 'blog_url'),
]