import uuid
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default=' ')
    description = models.TextField(max_length=1000, help_text='Enter a brief description')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default=' ')
    description = models.TextField(max_length=1000, help_text='Enter a brief description')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character '
                                      '<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    weight = models.FloatField(null=False, default=0)
    # manufacturer
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # subsection
    # category
    price = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID')
    product = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f'{self.product.name} {self.borrower}'

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),
                       ("staff_member_required", "Set user as employee"))
