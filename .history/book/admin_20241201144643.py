from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(B)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title'),}
