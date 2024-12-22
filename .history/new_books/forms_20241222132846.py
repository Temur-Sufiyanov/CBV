from django.forms.models import inlineformset_factory
from .models import Book, Author

AuthorBooksFormset = inlineformset_factory(Author, Book, fields=('name',), extra=1, deletr)