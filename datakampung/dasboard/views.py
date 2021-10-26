from django.shortcuts import render

# Create your views here.

# tampilan login
def login(request): 
    return render(request, 'index.html')

