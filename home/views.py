from django.shortcuts import render
from .models import Research, Author


def index(request):
    return render(
        request,
        'index.html',
        context={}
    )


def research(request):
    researches = Research.objects.all()
    return render(
        request,
        'research.html',
        context={'researches': researches}
    )


def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        'authors.html',
        context={'authors': authors}
    )


def about(request):
    return render(
        request,
        'about.html',
        context={}
    )


def editorial(request):
    return render(
        request,
        'editorial.html',
        context={}
    )


# Create your views here.
