from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm
from .forms import PostForm

def blogpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/blogpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug = post.slug)
    
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form
        })

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpage')
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})
