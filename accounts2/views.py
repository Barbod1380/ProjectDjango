from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def WhoAreYou(request):
    context = {}
    return render(request, 'Howiat.html', context)



def TregisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls/Teacher_Login')

    context = {'form': form}
    return render(request, 'accounts/Teacher_register.html', context)


def SregisterPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls/Student_Login')

    context = {'form': form}
    return render(request, 'accounts/Student_register.html', context)



def TLoginPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, password=password, email=email)
        if user is None:
             login(request, user)
             return redirect('polls/Teacher_Home')


    context = {'form':form}
    return render(request, 'accounts/Teacher_login.html', context)


def SLoginPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, password=password, email=email)

        if user is None:
            login(request, user)
            return redirect('polls/Student_Home')

    context = {'form': form}
    return render(request, 'accounts/Student_login.html', context)



def THomePage(requeest):
    return HttpResponse('Welcome our dear Teacher')

def SHomePage(request):
    return HttpResponse('Welcome our dear Student')









