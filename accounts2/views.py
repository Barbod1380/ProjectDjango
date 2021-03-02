from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm
from .forms import ProfileForm


def WhoAreYou(request):
    context = {}
    return render(request, 'Howiat.html', context)


def TregisterPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/Teacher_register.html', context)


def SregisterPage(request):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/Student_register.html', context)



def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    return render(request, 'accounts/products.html')

def customer(request):
    return render(request, 'accounts/customer.html')

