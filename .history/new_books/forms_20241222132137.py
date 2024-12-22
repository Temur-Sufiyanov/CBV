from django.forms.models import inlineformset_factory
from .models import Book

AuthorBooksFormset = inlineformset_factory(AuthorBook, fields=('name','author'))