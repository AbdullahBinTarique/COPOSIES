from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import SlugField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.apps import apps
from django.template.defaultfilters import default
from django.utils.text import slugify
from sqlalchemy.cyextension.processors import to_str
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
    slug = models.SlugField(max_length=20,unique=True)

    def save(self, *args, **kwargs):
        # Only generate slug if it’s not already set
        if not self.slug:
            self.slug = slugify(f"{self.fname} {self.lname}")
        super().save(*args, **kwargs)
    # def __str__(self):
    #     return   self.email

class Corelationdata(models.Model):
    subject = models.OneToOneField('Admin.SubjectDB',to_field='subject', on_delete=models.CASCADE,unique=True)
    data = models.JSONField(null=True)
    srno = models.AutoField(primary_key =True)




class CONAMES(models.Model):
    subject = models.OneToOneField('Admin.SubjectDB', to_field='subject',on_delete=models.CASCADE,unique=True)
    data = models.JSONField(null=True)
    srno = models.AutoField(primary_key =True)

    def __str__(self):
        return 'COS of '+to_str(self.subject)

class COPOAcheiveddata(models.Model):
    subject = models.ForeignKey('Admin.SubjectDB',to_field='subject',on_delete=models.CASCADE)
    copo = models.JSONField(null=True)
    data = models.JSONField(null=True)
    uploaded_by = models.ForeignKey('AdminUSERS',to_field='slug',on_delete=models.CASCADE,null=True)

    copoAch = models.JSONField(null=True)
    dataAch = models.JSONField(null=True)


class SubjectDB(models.Model):
    subject = models.CharField(unique=True, max_length=20, default="Subject")
    subject_id = models.CharField(max_length=20,unique=True)
    ia_th_lvl1_sc = models.PositiveSmallIntegerField(null=True,
                                                     validators=[MinValueValidator(1), MaxValueValidator(100)])
    ia_th_lvl2_sc = models.PositiveSmallIntegerField(null=True,
                                                     validators=[MinValueValidator(1), MaxValueValidator(100)])
    ia_th_lvl3_sc = models.PositiveSmallIntegerField(null=True,
                                                     validators=[MinValueValidator(1), MaxValueValidator(100)])
    #     pom =Percentage of marks
    ia_th_pom = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Sem_th_pom = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    srno = models.AutoField(primary_key=True,)

    NOCO =models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    NOPO =models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    NOPSO =models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    sem = models.PositiveSmallIntegerField(default = 1,validators=[MinValueValidator(1), MaxValueValidator(8)])
    subques = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    CONAMES = models.JSONField(null=True)



    def __str__(self):

        return   self.subject

