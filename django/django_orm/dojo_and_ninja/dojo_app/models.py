from django.db import models
from django.db.models.query_utils import select_related_descend

class Dojo (models.Model):
    title= models.CharField(max_length=45,default="moath11")
    age=models.IntegerField(default=200)
    desc=models.TextField(max_length=255,default="hello")


class Ninja (models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)

