from django.shortcuts import render, redirect

from blog.forms import NewPostForm
from blog.models import Post


def PostIndexView(request):
    if request.method == 'POST':
        fr = NewPostForm(request.POST)
        if fr.is_valid():
            fr.save()
            return redirect('blog_urls:blog_url')
    else:
        posts = Post.objects.all().order_by('-created_date')
        Form = NewPostForm()
    return render(request, 'index.html', {'tPosts':posts ,'tForm':Form})
