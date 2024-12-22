from django.forms.models import inlineformset_factory
from .models import Book

AuthorBooksFormset = inlineformset_factory( Book, fields=('name','author'))