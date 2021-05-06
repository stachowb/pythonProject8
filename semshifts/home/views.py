from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from drivers.models import Driver


class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['drivers'] = Driver.objects.all()
        return ctx