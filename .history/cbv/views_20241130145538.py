from django.shortcuts import render
from  django.views.generic import TemplateView
# Create your views here.

class MyView(TemplateView):
    template_name = 'cbv/index.html'

    
    def get_redirect_url(self, *args, **kwargs)