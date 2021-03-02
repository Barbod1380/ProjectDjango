from django.urls import path
from . import views


urlpatterns = [

    path('polls/Teacher_register/', views.TregisterPage),
    path('polls/Student_register/', views.SregisterPage),
    path('polls/Teacher_register/polls/Teacher_Login/', views.TLoginPage),
    path('polls/Student_register/polls/Student_Login/', views.SLoginPage),
    path('polls/Teacher_register/polls/Teacher_Login/polls/Teacher_Home', views.THomePage),
    path('polls/Student_register/polls/Student_Login/polls/Student_Home', views.SHomePage),
    path('polls/', views.WhoAreYou)

]


