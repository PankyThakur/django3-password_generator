from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request, 'generator/home.html')

def about(request):
     return render(request, 'generator/about.html')


def password(request):
    
    character = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        character.extend(list('QWERTYIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))  

    if request.GET.get('numbers'):
        character.extend(list('1234567890'))       
    
    length = int(request.GET.get('length',8))
    
    pwd = ''

    
    for i in range(length):
        pwd += random.choice(character)
    return render(request, 'generator/password.html',{'password':pwd})