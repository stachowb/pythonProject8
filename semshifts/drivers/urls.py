from django.urls import path
from .models import Driver

urlpatterns = [
    path('', DriversList.as_view(), name="drivers-list"),


]