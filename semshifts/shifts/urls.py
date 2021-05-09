from django.urls import path
from .views import ShiftsList, ShiftCreate

urlpatterns = [
    path('list', ShiftsList.as_view(), name="shifts-list"),
    path('add', ShiftCreate.as_view(), name="shifts-add")
]