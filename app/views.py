from django.shortcuts import render

# Create your views here.
def function(request):
    return render(request,'h1.html')

def function1(request):
    return render(request,'h2.html')