from django.contrib.auth.models import User
from django.db import models

class Bio(models.Model):
    Name=models.CharField(max_length=250, null=True)
    Date_of_birth=models.DateField(null=True)
    Address=models.CharField(max_length=500, null=True)
    Phone=models.CharField(max_length=11, null=True)
    Age=models.IntegerField(null=True)
    Degree=models.CharField(max_length=450, null=True)
    Email=models.EmailField(null=True)
    Skills=models.CharField(max_length=500, null=True)
    Freelance=models.BooleanField(default=True)
    Image=models.ImageField(upload_to='bio')


    def __str__(self):
        return '{}'.format(self.Name)

class Certificates(models.Model):
    Name=models.CharField(max_length=250, null=True)
    Description=models.CharField(max_length=250, null=True)
    Image=models.ImageField(upload_to='certificates')

    def __str__(self):
        return '{}'.format(self.Name)

class Projects(models.Model):
    Name=models.CharField(max_length=250, null=True)
    Description=models.CharField(max_length=250, null=True)
    Image=models.ImageField(upload_to='projects')

    def __str__(self):
        return '{}'.format(self.Name)