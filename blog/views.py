from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Shehryar',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'January 21, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'January 22, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
