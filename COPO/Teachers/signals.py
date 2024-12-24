# second_app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from sqlalchemy.orm.loading import instances

from Admin.models import AdminUSERS, SubjectDB
from .models import Teacher,Sem1,Sem2,Sem3,Sem4,Sem5,Sem6,Sem7,Sem8

@receiver(post_save, sender=Sem1)
@receiver(post_save, sender=Sem2)
@receiver(post_save, sender=Sem3)
@receiver(post_save, sender=Sem4)
@receiver(post_save, sender=Sem5)
@receiver(post_save, sender=Sem6)
@receiver(post_save, sender=Sem7)
@receiver(post_save, sender=Sem8)
@receiver(post_save, sender=Teacher)

def create_or_update_Teachers_model(sender, instance, created, **kwargs):
    if sender ==AdminUSERS:
        if created:

            # Create a corresponding record in SecondAppModel

            Teacher.objects.create(

                email=instance.email  ,
                Username=instance.username,

            )


            # print(instance)
        # else:
        #     # Update multiple fields in an existing record
        #     auser = AdminUSERS.objects.filter(email=instance.email).first()
        #     second_instance = Teacher.objects.filter(email=auser.email).first()
        #     if second_instance:
        #         second_instance.Username = auser.username
        #         second_instance.email = instance
        #         # second_instance.subject = instance.subject
        #         second_instance.save()
    elif sender == Sem1:
        if created:
            # Create a corresponding record in SecondAppModel
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem = 1,
            )
    elif sender == Sem2:
        if created:
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem=2,
            )
    elif sender == Sem3:
        if created:
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem=3,
            )
    elif sender == Sem4:
        if created:
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem=4,
            )
    elif sender == Sem5:
        if created:
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem=5,
            )
    elif sender == Sem6:
        if created:
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem=6,
            )
    elif sender == Sem7:
        if created:
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem=7,
            )
    elif sender == Sem8:
        if created:
            SubjectDB.objects.create(
                subject=instance.Subject,
                sem=8,
            )