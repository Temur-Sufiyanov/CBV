from django import forms
from .models import Book

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'genre':forms
        }