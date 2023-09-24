from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = "home.html" 

def index(request):
    return render(request, "home.html")