from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import Video_form
from .models import Video



def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls/Student_Login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
def LoginPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, password=password, email=email)
        if user is None:
             login(request, user)
             return redirect('polls/Home')


    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def HomePage(request):
    all_video = Video.objects.all()
    if request.method == 'POST':
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded Succesfully </h1>")
    else:
        form=Video_form
    return render(request, 'accounts/index.html', {"form":form})

























