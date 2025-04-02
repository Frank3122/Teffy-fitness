from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"gym.html")

def method (request):
    return render (request, "gym website2.html")

def test (request):
    return render (request, "gym website3.html")

def story (request):
    return render(request, "gym website4.html")

def sports (request):
    return render (request, "gym website5.html")

def fitness (request):
    return render (request, "gym website 6.html")

def academy (request):
    return render (request, "gym website7.html")

def events (request):
    return render (request, "gym website8.html")

def forms (request):
    return render (request, "gym Loginpage.html")

def gymform (request):
    return render (request,"forms.html")