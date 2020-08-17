from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('news.urls')),
    path('polls/', include('polls.urls')),
]
