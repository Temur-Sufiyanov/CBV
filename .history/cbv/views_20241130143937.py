from django.shortcuts import render
from  django.views.generic import TemplateView, red
# Create your views here.

class MyView(TemplateView):
    template_name = 'cbv/index.html'
