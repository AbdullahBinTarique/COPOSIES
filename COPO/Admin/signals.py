# second_app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver

import Teachers
from Teachers.models import Teacher
from .models import AdminUSERS, SubjectDB, CONAMES


@receiver(post_save, sender=CONAMES)
def create_or_update_Teachers_model(sender, instance, created, **kwargs):
    if created:

        inst=  SubjectDB.objects.get(subject = instance.subject)
        inst.CONAMES = instance.data
        inst.save()
    else:
        inst = SubjectDB.objects.get(subject=instance.subject)
        inst.CONAMES = instance.data
        inst.save()

