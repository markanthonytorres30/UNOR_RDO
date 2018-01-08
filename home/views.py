from django.shortcuts import render
from .models import  Question

def index(request):

    question = Question.question_text

    return render(
        request,
        'index.html',
        context={'question':'hahahah'}
    )
# Create your views here.
