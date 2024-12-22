from django.urls import path
from .views import MyView
from djan
urlpatterns = [
    path('', MyView.as_view(), name='home'),
    path('rdk', ),
]
