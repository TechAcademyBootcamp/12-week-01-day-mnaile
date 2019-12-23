from django.db import models

# Create your models here.

class Login(models.Model):

    admin = models.ForeignKey('Admin', on_delete = models.CASCADE)

    email = models.EmailField()
    password = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    zip = models.CharField(max_length=250)
    check = models.BooleanField(default=False)


    def __str__(self):
        return self.email

class Admin(models.Model):
    fullname = models.CharField(max_length=250)

    def __str__(self):
        return self.fullname