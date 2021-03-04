from django.urls import path
from . import views
from .views import HomePage2, QuestionPage, AddQuestion


urlpatterns = [

    path('polls/polls/Login/', views.LoginPage),
    path('polls/polls/Login/polls/Home', views.HomePage),
    path('polls/', views.registerPage),
    path('polls/polls/Login/polls/Questions', HomePage2.as_view(), name='home'),
    path('polls/polls/Login/polls/Questions/<int:pk>', QuestionPage.as_view(), name='Q-detail'),
    path('polls/polls/Login/polls/AddQuestions', AddQuestion.as_view(), name='newq'),

]


