from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def information(request):
    return render(request,'info.html')

def table(request):
    return render(request,'tables.html')

def form(request):
    return render(request,'form.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'registration.html')


