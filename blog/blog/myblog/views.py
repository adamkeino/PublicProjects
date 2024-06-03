from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Function based view
#   def home(request):
#     return render(request, "home.html", {})

class HomeView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetail(DetailView):
    model = Post
    template_name = "blog_details.html"
