from django.urls import path
from . import views

urlpatterns = [
    path('register-student/', views.registerStudent, name='registerStudent'),
    path('register-university/', views.registerUniversity, name='registerUniversity'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]