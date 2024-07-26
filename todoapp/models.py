from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerprofilePic/', null=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10, null=False)


class Tasks(models.Model):
    name=models.CharField(max_length=40)
    date=models.DateField()
    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.title
