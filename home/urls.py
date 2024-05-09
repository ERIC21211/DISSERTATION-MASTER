from django.urls import path
from . import views
from .views import add_post, like_post

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactform, name='contactform'),
    path('university/<int:id>/', views.chat_detail_view, name='chat'),
    path('search/', views.search, name='search'),
    path('add-post/', add_post, name='add_post'),  # URL for adding a new post
    path('like-post/<int:post_id>/', like_post, name='like_post'),
]