from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Shift


@receiver(pre_save, sender=Shift)
def pre_save_calc_wages(sender, instance, created, **kwargs):
    pass