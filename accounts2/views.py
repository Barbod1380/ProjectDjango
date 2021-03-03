from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import Video_form
from .models import Video




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


def THomePage(request):
    all_video = Video.objects.all()
    if request.method == 'POST':
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded Succesfully </h1>")
    else:
        form=Video_form
    return render(request, 'accounts/index.html', {"form":form})


def SHomePage(request):
    return HttpResponse('Welcome our dear Student')









