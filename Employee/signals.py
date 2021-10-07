from django.contrib.auth.models import User
from .models import EmployeeProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError,transaction

@receiver(post_save,sender=User)
def create_employee_profile(sender,instance,created,**kwargs):
    if not created:
        if instance.is_staff:
            try:
                with transaction.atomic():
                    EmployeeProfile.objects.create(user=instance)
                    instance.employeeprofile.save()
            except IntegrityError:
                instance.employeeprofile.save()
