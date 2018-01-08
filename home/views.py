from django.shortcuts import render
from .models import  Question

def index(request):

    question = Question.question_text

    return render(
        request,
        'index.html',
        context={'question':'hahahah'}
    )

def research(request):

    return render(
        request,
        'research.html',
        context={'question':hahahah}
    )

def authors(request):
    return render(
        request,
        'authors.html',
        context=None
    )

# Create your views here.
