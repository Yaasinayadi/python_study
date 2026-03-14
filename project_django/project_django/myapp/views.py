from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
# Create your views here.
def index(request):
  features = Feature.objects.all()
  return render(request, 'index.html', {'features': features})
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())

    return render(request, 'counter.html', {'amount': amount_of_words})
def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password1 = request.POST['password1']

    if password == password1:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'email exists deja')
        return redirect('register') 
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'username existe deja')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else:
      messages.info(request, 'MDP non identiques')
      return redirect('register')
  else:
    return render(request, 'register.html')
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Cred invalid')
      return render(request, 'login.html')
  else:  
    return render(request, 'login.html')
def logout(request):
  auth.logout(request)
  return redirect('index')