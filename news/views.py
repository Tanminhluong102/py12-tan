import news as news
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    context = {}
    return render(request, 'index.html', context)


def category(request):
    context = {}
    return render(request, 'category.html', context)


def blog(request):
    context = {}
    return render(request, 'blog.html', context)


def blog_details(request):
    context = {}
    return render(request, 'blog_details.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def elements(request):
    context = {}
    return render(request, 'elements.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def sign_up(request):
    context = {}
    return render(request, 'sin-up.html', context)


def my_Main(request):
    context = {}
    return render(request, 'main.html', context)


def post_details(request):
    context = {}
    return render(request, 'post_details.html', context)


def feedback(request):
    if request.method == 'POST':
        ls = request.POST.dict()
        content = ls.get('content')
        name = ls.get('name')
        email = ls.get('email')
        subject = ls.get('subject')
        # print(content,name,email,subject)
        Feedback.objects.create(content=content, name=name, email=email, subject=subject)
        return HttpResponse("<h1>Success</h1>")
    return render(request, 'contact.html')
def search(request):
    if request.method == 'POST':
        search = request.POST.dict().get('search').lower().split()
        news = New.objects.all()
        res  = []
        for new in news:
            for text in search:
                if text in new.title or text in new.context:
                    res.append(new)
                    break
    return render(request,'search.html', {'news':res})
