from django.urls import path
from . import views


urlpatterns = [

    path('polls/polls/Login/', views.LoginPage),
    path('polls/polls/Login/polls/Home', views.HomePage),
    path('polls/', views.registerPage)

]


