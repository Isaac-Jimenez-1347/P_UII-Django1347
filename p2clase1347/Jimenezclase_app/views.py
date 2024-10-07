from django.shortcuts import render
def hola(request):
    return render(request,'index.html')

def Mi_mama(request):
    return render(request,'mama.html')