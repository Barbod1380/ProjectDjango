from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('polls/Teacher_register/', views.TregisterPage),
    path('polls/Student_register/', views.SregisterPage),
    path('polls/', views.WhoAreYou)

]

