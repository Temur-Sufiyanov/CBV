from django.shortcuts import render
from  django.views.generic import TemplateView, RedirectView
# Create your views here.

class MyView(TemplateView):
    template_name = 'cbv/index.html'
    
class MyRedirectView(RedirectView):
    url
