from email.policy import default

from django.db import models
from sqlalchemy import false
from django.core.validators import MaxValueValidator, MinValueValidator
from  Admin.models import AdminUSERS,SubjectDB



# Create your models here.
class Teacher(models.Model):
    srno = models.AutoField(primary_key = True)
    Username = models.CharField(max_length=30 )
    email = models.ForeignKey(AdminUSERS,to_field='email' ,on_delete=models.CASCADE,default='name@gmail/sies.edu.in' )
    subject = models.CharField(max_length=20)
    subques = models.PositiveSmallIntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(100)])

#     threshold set by teacher SC is students Scoring
    ia_th_lvl1_sc = models.PositiveSmallIntegerField(null=True  ,validators=[MinValueValidator(1), MaxValueValidator(100)])
    ia_th_lvl2_sc = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    ia_th_lvl3_sc = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])

#     pom =Percentage of marks
    ia_th_pom = models.PositiveSmallIntegerField(null=True,  validators=[MinValueValidator(1), MaxValueValidator(100)])

#     threshold set by teacher SC is students Scoring
    sem_th_lvl1_sc = models.PositiveSmallIntegerField(null=True,  validators=[MinValueValidator(1), MaxValueValidator(100)])
    sem_th_lvl2_sc = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    sem_th_lvl3_sc = models.PositiveSmallIntegerField(null=True,  validators=[MinValueValidator(1), MaxValueValidator(100)])

#     pom =Percentage of marks
    sem_th_pom = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.Username


class Branch(models.Model):

    branch = models.CharField(max_length=50,primary_key=True,default='SIES')


    def __str__(self):
        return self.branch

class Batch(models.Model):

    batch = models.CharField(max_length=5,primary_key=True,default='00-00')

    def __str__(self):
        return self.batch


class Students(models.Model):
    srno = models.AutoField
    name = models.CharField(max_length=50,null=False,default='Name')
    prn  =  models.CharField(max_length=8,primary_key=True,default='Prn')
    branch  = models.ForeignKey(Branch,to_field='branch', on_delete=models.CASCADE,default='SIES')
    batch = models.ForeignKey(Batch,to_field='batch' , on_delete=models.CASCADE,default='00-00')

    def __str__(self):
        return self.name + ' ' +self.prn



class Sem1(models.Model):
     Subject = models.CharField(max_length=20,unique = True)
     code = models.CharField(max_length=20,unique = True)

     def __str__(self):
         return self.Subject + ' ' + self.code


class Sem2(models.Model):
    Subject = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.Subject + ' ' + self.code


class Sem3(models.Model):
    Subject = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.Subject + ' ' + self.code


class Sem4(models.Model):
    Subject = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.Subject + ' ' + self.code


class Sem5(models.Model):
    Subject = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.Subject + ' ' + self.code


class Sem6(models.Model):
    Subject = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.Subject + ' ' + self.code


class Sem7(models.Model):
    Subject = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.Subject + ' ' + self.code


class Sem8(models.Model):
    Subject = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.Subject + ' ' + self.code
