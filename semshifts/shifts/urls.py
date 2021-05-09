from django.urls import path
from .views import ShiftList, ShiftCreate, ShiftUpdate,ShiftDelete

urlpatterns = [
    path('list/', ShiftList.as_view(), name="shifts-list"),
    path('add/', ShiftCreate.as_view(), name="shifts-add"),
    path('edit/<int:pk>', ShiftUpdate.as_view(), name="shifts-update"),
    path('delete/<int:pk>', ShiftDelete.as_view(), name="shifts-delete")
]