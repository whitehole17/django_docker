from django.db import models
from django import forms

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']