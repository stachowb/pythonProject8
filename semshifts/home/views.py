from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from drivers.models import Driver
from .forms import ShiftFileForm
from django.urls import reverse


class HomeView(FormView):
    template_name = "home.html"
    form_class = ShiftFileForm
    success_url = reverse("home")