from django.urls import path 
from .views import IndexView, B

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]

