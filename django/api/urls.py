from django.urls import path
from .views import heat_data

urlpatterns = [
    path('heat/', heat_data.get),
]
