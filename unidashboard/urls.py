from django.urls import path
from . import views

urlpatterns = [
    path('university-dashboard/', views.university_dashboard, name='unidashboard'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('university_page/<int:id>/', views.university_detail_view, name='university_detail_view'),
]