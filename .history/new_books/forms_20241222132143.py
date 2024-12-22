from django.forms.models import inlineformset_factory
from .models import Book, A

AuthorBooksFormset = inlineformset_factory(Author, Book, fields=('name','author'))