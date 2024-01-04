from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import runapp

# faq=""
# Create your views here.
def reg(request):

    if request.method=='POST':
        faq=request.POST['myInput']
        poem=runapp.inp(faq)
        return render(request,'show.html',{'faq':faq,'poem':poem})
    return render(request,'reg.html')

# def create(request):
#     poem=runapp.inp(faqpass)
#     print(faqpass)
#     print(poem)
#     return render(request,'show.html' ,{'faq':faqpass,'poem':poem} )