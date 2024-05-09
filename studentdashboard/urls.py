from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='studentdashboard'),
    path('studentname/', views.student_name, name='studentname'),
    path('studentcourse/', views.student_course, name='studentcourse'),
    path('studentcountry/', views.student_country, name='studentcountry'),
]