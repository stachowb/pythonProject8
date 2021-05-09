from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Shift
from .forms import CreateShiftForm


class ShiftsList(ListView):
    model = Shift
    paginate_by = 10
    context_object_name = "shifts"
    template_name = "shifts/shift-list.html"


class ShiftCreate(CreateView):
    model = Shift
    template_name = "shift-add.html"
    form = CreateShiftForm()
