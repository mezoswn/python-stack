from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.TimeField(auto_now_add= True)
    updated_at = models.TimeField(auto_now= True)
    desc= models.CharField(max_length=255)


class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojos , related_name='ninjas', on_delete= models.CASCADE)
    created_at = models.TimeField(auto_now_add= True)
    updated_at = models.TimeField(auto_now= True)