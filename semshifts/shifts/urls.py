from django.urls import path
from .views import ShiftList, ShiftCreate

urlpatterns = [
    path('list/', ShiftList.as_view(), name="shifts-list"),
    path('add/', ShiftCreate.as_view(), name="shifts-add")
]