from django.urls import path
from .views import (HomeView, AuthorView, AuthorCreateview)

app_name = 'books'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('author/', AuthorView.as_view(), name='authors'),
    path('author/add/'),
]