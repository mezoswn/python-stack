from django.db import models
from django.db.models.fields import CharField, DateField, TextField, related, datetime
from time import strftime


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show Network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show Description should be at least 10 characters"
        return errors




# Create your models here.



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description= models.TextField()
    objects = BlogManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


