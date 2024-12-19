from django.db import models

# Create your models here.
class USERS(models.Model):
    serial = models.AutoField
    email = models.CharField(max_length=100,default='name@gmail/sies.edu.in')
    usertype = models.CharField(max_length=2,default='TE')
    password = models.CharField(max_length=15,default='Password')
    fname = models.CharField(max_length=10,default='FirstName')
    lname = models.CharField(max_length=10,default='LastName')



    def __str__(self):
        return self.email