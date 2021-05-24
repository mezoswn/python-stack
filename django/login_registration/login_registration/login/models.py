from typing import ClassVar
from django.db import models
from django.db.models.query import FlatValuesListIterable

# Create your models here.
class Users (models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def register (name, passwd):
    Users.objects.create(name = name, password = passwd)

def check_user (name, passwd):
    user = Users.objects.filter(name = name)
    if user == None:
        return False
    if user [0].password == passwd:
        return True
    return False