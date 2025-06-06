from django.shortcuts import render
from .models import Post

def categoria(request, categoria):
        # implementar función obtener_posts_por_categoria
    posts = obtener_posts_por_categoria(categoria)
    return render(request, 'AppBlog/categoria.html', {'posts': posts})

def index(request):
    posts = Post.objects.all()
    return render(request, 'AppBlog/index.html', {'posts': posts})

def detalle_post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'AppBlog/detalle_post.html', {'post': post})