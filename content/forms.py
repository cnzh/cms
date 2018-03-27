from django.forms import ModelForm, Textarea
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': 25}),
        }
