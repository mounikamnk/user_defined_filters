from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'Hai Mounika HOW ARE YOU'}

    
    return render(request,'usdf.html',d)
