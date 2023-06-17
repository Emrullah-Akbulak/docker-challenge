from django.urls import path, include
from django.contrib import admin
from .views import helloWorld

urlpatterns = [
    path('api/', include('api.urls')),
    path('', helloWorld),
    path('admin/', admin.site.urls),
]
