from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User



# Create your views here.
def home(request):
    return render(request,'home.html')

def task(request):
    return render(request,'task.html')

#def singUp(request):
  # print(request.POST)
  #user = User.objects.create_user(
     #username=request.POST['username'], password=request.POST['password1'])
  #user.save()
  #return redirect('task')

  #return render(request, 'singUp.html', {
        #'form': UserCreationForm
    #})
def singUp(request):
    if request.method == 'GET':
        return render(request, 'singUp.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('task')
            except:
                return render(request, 'singUp.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe' 
                })
            
def signgin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], 
                            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario y contraseña no coinciden'
        })
        else:
            login(request, user)
            return redirect('task')
def signout(request):
    logout(request)
    return redirect('home')