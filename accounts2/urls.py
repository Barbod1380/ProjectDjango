from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('polls/Teacher_register/', views.TregisterPage),
    path('polls/Student_register/', views.SregisterPage),
    path('polls/Teacher_register/Teacher_Login', views.TLoginPage),
    path('polls/Student_register/Student_Login', views.SLoginPage),
    path('polls/', views.WhoAreYou)

]


