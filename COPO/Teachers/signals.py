# second_app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from Admin.models import AdminUSERS
from .models import Teacher

@receiver(post_save, sender=AdminUSERS)
def create_or_update_Teachers_model(sender, instance, created, **kwargs):
    if created:

        # Create a corresponding record in SecondAppModel
        auser = AdminUSERS.objects.filter(email = instance.email).first()
        Teacher.objects.create(

            email=auser ,
            Username=auser.username
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

