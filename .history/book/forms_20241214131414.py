from django import forms
from .models import Book

class AddForm(forms.ModelForm):
    
    class Meta