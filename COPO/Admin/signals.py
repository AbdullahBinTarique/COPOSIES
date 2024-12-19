# second_app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from Teachers.models import Teacher
from .models import AdminUSERS, SubjectDB


@receiver(post_save, sender=Teacher)
def create_or_update_Teachers_model(sender, instance, created, **kwargs):
    if created:
        pass
        # Create a corresponding record in SecondAppModel
        # SubjectDB.objects.create(
        #     # email=instance.email,
        #     # Username=instance ,
        #
        # )
    else:
        pass
        # Update multiple fields in an existing record
        # second_instance = Teacher.objects.filter(email=instance).first()
        # if second_instance:
            # second_instance.Username = instance.username
            # second_instance.email = instance
            # second_instance.subject = instance.subject,
            # second_instance.save()
