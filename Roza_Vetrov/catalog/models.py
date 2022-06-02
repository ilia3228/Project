import uuid
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Product(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character '
                                      '<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

class ProductInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID')
    product = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

