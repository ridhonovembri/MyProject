from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hrdept',include('hrdept.urls')),
    path('hremployee',include('hremployee.urls')),
]
