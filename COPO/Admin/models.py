from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import SlugField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.apps import apps

# from Teachers.models import Sem1, Sem2, Sem3, Sem4, Sem5, Sem6, Sem7, Sem8, Batch, Branch


# Create your models here.
class AdminUSERS(models.Model):

    email = models.CharField(max_length=100, default='name@gmail/sies.edu.in',unique=True,primary_key=True)
    usertype = models.CharField(max_length=2, default='TE')
    password = models.CharField(max_length=15, default='Password')
    fname = models.CharField(max_length=10, default='FirstName')
    lname = models.CharField(max_length=10, default='LastName')
    username = models.CharField(max_length=15, default='UserName')
    # subject = models.CharField(max_length=20, default='Subject')
    sem =   models.PositiveSmallIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(8)] )
    slug = models.SlugField(max_length=20,default='')

    def __str__(self):
        return   self.email

class SubjectDB(models.Model):


    srno = models.AutoField(primary_key = True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null = True )
    object_id = models.PositiveIntegerField(null=True)
    subjects = GenericForeignKey('content_type','object_id')
    batch = models.ForeignKey('Teachers.Batch',on_delete=models.CASCADE,default = '00-00')
    branch = models.ForeignKey('Teachers.Branch',on_delete=models.CASCADE,default = 'SIES')
    email = models.ForeignKey(AdminUSERS,to_field='email', on_delete=models.CASCADE,default='Email')
    # CO1 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)],default= 0)
    # CO2 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)],default= 0)
    # CO3 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)],default= 0)
    # CO4 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)],default= 0)
    # CO5 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)],default= 0)
    # CO6 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)],default= 0)
    COs = models.TextField(default=' ')



