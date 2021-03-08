from django.urls import path
from . import views
from .views import THomePage, TQuestionPage, TEachQuestionPage, TAddQuestionPage, SHomePage, SQuestionPage, SEachQuestionPage, TSendedAnswerPage


urlpatterns = [

    path('', views.Page0, name='Page0'),
    path('Tlogin/', views.TeacherLoginpage, name='Tlogin'),
    path('THome/', THomePage.as_view(), name='THP'),
    path('THome/TAddQuestion/', TAddQuestionPage.as_view(), name='TAQ'),
    path('THome/TQuestionsDetail/', TQuestionPage.as_view(), name='TQD'),
    path('THome/Video/', views.teacherVideos, name='TV'),
    path('THome/Video/VideoDetail/<int:video_id>/', views.Teacher_Video_Detail, name='TVD'),
    path('THome/Video/ADDVideo/', views.teacherAddVideos, name='TAV'),
    path('THome/TQuestionsDetail/<int:pk>/', TEachQuestionPage.as_view(), name='TEQ'),
    path('THome/SendedAnswer/', TSendedAnswerPage.as_view(), name='TSA'),
    path('THome/SendedAnswer/<str:q_title>', views.TeachSendedAnswer, name='TSAP'),



    path('Slogin/', views.StudentLoginpage, name='Slogin'),
    path('SHome/', SHomePage.as_view(), name='SHP'),
    path('SHome/SendAnswer/', views.SendAnsPage, name='SAP'),
    path('SHome/Videos/', views.studentVideos, name='SAP'),
    path('SHome/Videos/VideoDetail/<int:video_id>/', views.Student_Video_Detail, name='SVD'),
    path('SHome/SQuestionsDetail/', SQuestionPage.as_view(), name='SQD'),
    path('SHome/SQuestionsDetail/<int:pk>', views.SEachQuestionPage, name='SEQ'),
    path('SHome/SQuestionsDetail/<int:pk>/', views.SSendAnsPage, name='SEQ'),


    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),

]
