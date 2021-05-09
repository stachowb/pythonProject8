from django.views.generic.edit import FormView
from .forms import ShiftFileForm
from django.urls import reverse


class HomeView(FormView):
    template_name = "home.html"
    form_class = ShiftFileForm
    success_url = "/home"

    # def dispatch(self, request, *args, **kwargs):
    #     request.session['csv_file'] = csv_file
    #     return super().dispatch(request, *args, **kwargs)