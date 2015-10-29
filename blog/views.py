from django.shortcuts import render
from django.utils import timezone
from .models import Postear
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
     posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
     return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})