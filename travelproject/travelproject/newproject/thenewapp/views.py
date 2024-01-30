from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team


def demo(request):
    obj = place.objects.all()
    object2 = team.objects.all()
    #name="india"
    #return render(request,'home.html',{'obj':name})
    return render(request, 'index.html', {'result':obj,'result1':object2})

#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #add = x + y
    #sub = x - y
    #div = x / y
    #mul = x * y
    #return render(request,'about.html',{'addition': add,'subtraction': sub,'division': div,'multiplication': mul})
    #return render(request, 'about.html', )
    #return render(request, 'about.html', {})
    #return render(request,'about.html',{})

