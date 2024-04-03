from .models import Post
from django.views.generic import ListView, DetailView



class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/index.html'
    context_object_name = 'news'



class PostDetailView(DetailView):
    model = Post
    template_name = 'news/details.html'
    context_object_name = 'new'

