from django.http import HttpResponse
from django.shortcuts import render


def demo(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,'contact.html')
