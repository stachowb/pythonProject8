from django.urls import path
from .views import ShiftsList

urlpatterns = [
    path('list', ShiftsList.as_view(), name="shifts-list")
]