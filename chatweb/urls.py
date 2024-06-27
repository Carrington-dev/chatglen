from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("chat/", include("chatty.urls")),
    path('admin/', admin.site.urls),
]
