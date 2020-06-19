from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render (request, 'generator/home.html', {"welcomemessage":"How are you"})
def eggs(request):
    return HttpResponse("Eggs are not good for health. Dont eat eggs")
def password(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('Length',8))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=:;/?><|\''))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render (request, 'generator/password.html',{'password':thepassword})
def about(request):
    return render (request, 'generator/about.html',)
