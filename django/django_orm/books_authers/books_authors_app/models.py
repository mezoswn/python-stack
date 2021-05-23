from django.db import models
from django.db.models.fields import CharField, TextField, TimeField

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    book = models.ManyToManyField(Books , related_name="books_authors")
    notes = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)