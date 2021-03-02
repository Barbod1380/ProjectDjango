from django.urls import path
from . import views


urlpatterns = [

    path('polls/Teacher_register/', views.TregisterPage),
    path('polls/Student_register/', views.SregisterPage),
    path('polls/Teacher_register/polls/Teacher_Login/', views.TLoginPage),
    path('polls/Student_register/polls/Student_Login/', views.SLoginPage),
    path('polls/', views.WhoAreYou)

]


