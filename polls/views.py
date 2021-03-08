from django.shortcuts import render, redirect
from .forms import BookForm, CreateStudentForm, CreateTeacherForm, CreateVideo, Grade
from .models import ANS, Question, Videos
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def Page0(request):
    return render(request, 'EhrazHowiat.html')


class SHomePage(ListView):
    model = Question
    template_name = 'polls2/Studenthome.html'
class THomePage(ListView):
    model = Question
    template_name = 'polls2/Teacherhome.html'




class TSendedAnswerPage(ListView):
    model = Question
    template_name = "polls2/TeacherSendedAns.html"


def TeachSendedAnswer(request, q_title):
    books = ANS.objects.filter(QuestionName=q_title)
    form = Grade
    context = {'books': books, 'form': form}
    return render(request, "polls2/TQuestionsAnsTable.html", context)





class TQuestionPage(ListView):
    model = Question
    template_name = 'polls2/Teacherquestions.html'
class SQuestionPage(ListView):
    model = Question
    template_name = 'polls2/Studentquestions.html'



class TEachQuestionPage(DetailView):
    model = Question
    template_name = 'polls2/Teachereachquestions.html'




def SEachQuestionPage(request, pk):
    question = Question.objects.get(id=pk)
    context = {'question': question}
    return render(request, 'polls2/Studenteachquestions.html', context)





def teacherVideos(request):
    videos = Videos.objects.all()
    context = {'videos':videos}
    return render(request, 'polls2/TVideoscaption.html', context)
def studentVideos(request):
    video = Videos.objects.all()
    context = {'videos': video}
    return render(request, "polls2/SVideocaption.html", context)




def teacherAddVideos(request):
    form = CreateVideo()
    if request.method == "POST":
        form = CreateVideo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your File has been uploaded')
    context = {'form':form}
    return render(request, 'polls2/TeacherUploadVideo.html', context)

def Teacher_Video_Detail(request, video_id):
    vid = Videos.objects.get(id=video_id)
    context = {'video': vid}
    return render(request, 'polls2/TeacherVideoDetail.html', context)

def Student_Video_Detail(request, video_id):
    vid = Videos.objects.get(id=video_id)
    context = {'video': vid}
    return render(request, 'polls2/StudentVideoDetail.html', context)




class TAddQuestionPage(CreateView):
    model = Question
    template_name = 'polls2/Teacheraddquestion.html'
    fields = '__all__'


def SendAnsPage(request):
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/books/')
    else:
        form = BookForm()
    return render(request, 'polls2/upload_book.html', {'form':form})

def TAnsPage(request):
    books = ANS.objects.all()
    return render(request, 'polls2/book_list.html', {'books': books})


def SSendAnsPage(request, pk):
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Uploaded Succesfully")
    else:
        form = BookForm()
    return render(request, 'polls2/upload_book.html', {'form': form})




def StudentLoginpage(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
                username = request.POST.get('UserName')
                password = request.POST.get('Password')
                studentnumber = request.POST.get('StudentNumber')
                email = request.POST.get('Email')
                user = authenticate(request, username=username, password=password, studentnumber=studentnumber, email=email)

                if user is not None:
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/SHome/')
                else:
                    return HttpResponse("ERROR:   User Does Not Exist")
    else:
        form = CreateStudentForm
    return render(request, 'polls2/Studentlogin.html', {'form':form})
def TeacherLoginpage(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            username = request.POST.get('UserName')
            password = request.POST.get('Password')
            email = request.POST.get('Email')
            user = authenticate(request, username=username, password=password, email=email)

            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/THome/')
            else:
                return HttpResponse("ERROR:   User Does Not Exist")
    else:
        form = CreateTeacherForm

    return render(request, 'polls2/Teacherlogin.html', {'form':form})



def book_list(request):
    books = ANS.objects.all()
    return render(request, 'polls2/book_list.html', {'books':books})
def upload_book(request):
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/books/')
    else:
        form=BookForm()
    return render(request, 'polls2/upload_book.html', {'form':form})



