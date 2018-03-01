from django.shortcuts import render


def login(request):
    return render(
        request,
        'login.html',
        context={}
    )

# Create your views here.
