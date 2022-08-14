from django.shortcuts import render
from .models import Post

# Route for home page


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home Page'
    }
    return render(request, 'blog/home.html', context)


# Route for about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
