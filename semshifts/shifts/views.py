from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Shift
from .forms import CreateShiftForm


class ShiftList(ListView):
    model = Shift
    paginate_by = 50
    context_object_name = "shifts"
    template_name = "shifts/shift-list.html"


class ShiftCreate(SuccessMessageMixin, CreateView):
    model = Shift
    template_name = "shift-add.html"
    form_class = CreateShiftForm
    # fields = ['company', 'driver', 'clock_in', 'clock_out', 'km_driven']
    success_message = "Shift has been created"


class ShiftUpdate(SuccessMessageMixin, UpdateView):
    model = Shift
    template_name = "shift-add.html"
    form = CreateShiftForm
    # fields = ['driver', 'clock_in', 'clock_out', 'km_driven']
    success_message = "Shift has been updated"


class ShiftDelete(SuccessMessageMixin, DeleteView):
    model = Shift
    template_name = "shift-delete.html"
    success_url = reverse_lazy("shifts-list")
    success_message = "Shift has been deleted"



