from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls,),
    path("", include("home.urls")),
    path("auth/", include("authentication.urls")),
    path("student/", include("studentdashboard.urls")),
    path("university/", include("unidashboard.urls")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
