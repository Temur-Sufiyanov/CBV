from django.urls import path
from .views import MyView
from django.views.generic import Red
urlpatterns = [
    path('', MyView.as_view(), name='home'),
    path('rdk', ),
]
