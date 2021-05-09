from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView
from .models import Shift
from .forms import CreateShiftForm


class ShiftsList(ListView):
    model = Shift
    paginate_by = 50
    context_object_name = "shifts"
    template_name = "shifts/shift-list.html"


class ShiftCreate(CreateView):
    model = Shift
    template_name = "shift-add.html"
    form = CreateShiftForm
    fields = ['driver', 'clock_in', 'clock_out', 'km_driven']
    success_url = "/shifts/list"




