from django.db import models
from time import localtime, strftime
import re

# Create your models here.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        lisOfEmails = Users.objects.filter(email=postData['email'])
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(lisOfEmails):
            errors['email'] = "Email is Aleardy exist"

        # add keys and values to errors dictionary for each invalid fieldcopy
        if len(postData['firstname']) < 2:
            errors["firstname"] = "User first should be at least 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "User Last name should be at least 2 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "User Password should be at least 8 characters"
        todayTime= strftime("%Y-%m-%d", localtime())
        postTime = postData['birth_date']
        todayTimeList = todayTime.split("-")
        postTimeList = postTime.split("-")
        if (todayTimeList[0] <= postTimeList[0]):
            if  (todayTimeList[1] <= postTimeList[1]):
                if (todayTimeList[2] < postTimeList[2]):
                    errors["birth_date"] = "You are not born yet!!!"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dateOfBirth = models.DateField(null=True, verbose_name='Date of Birth')
    objects = BlogManager()

