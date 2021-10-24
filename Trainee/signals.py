from django.contrib.auth.models import User
from .models import TraineeProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError,transaction

@receiver(post_save,sender=User)
def create_trainee_profile(sender,instance,created,**kwargs):
    if not created:
        if not instance.is_staff:
            try:
                with transaction.atomic():
                    TraineeProfile.objects.create(user=instance)
                    instance.traineeprofile.save()
            except IntegrityError:
                pass
    else:
        pass
