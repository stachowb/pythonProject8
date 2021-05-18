from django.urls import path
from .views import ShiftList, ShiftCreate, ShiftUpdate,ShiftDelete

urlpatterns = [
    path('list/', ShiftList.as_view(), name="shifts-list"),
    path('add/', ShiftCreate.as_view(), name="shifts-add"),
    path('edit/<slug:slug>/', ShiftUpdate.as_view(), name="shifts-edit"),
    path('delete/<slug:slug>/', ShiftDelete.as_view(), name="shifts-delete")
]