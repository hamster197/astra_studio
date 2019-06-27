from django import forms

from blog.models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        fields = ('text',)
        model = Post