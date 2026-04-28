from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostForm

# Create your views here.
def hello_view(request):
    return render(request, 'main/hello.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'main/post_list.html', {'posts': posts})

def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'main/post_form.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post_list')