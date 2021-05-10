from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Shift


@receiver(post_save, sender=Shift)
def post_save_calc_wages(sender, instance, created, **kwargs):
    if created:
        instance.above_200 = instance.km_driven - 200
        instance.shift_length = instance.clock_out - instance.clock_in
        instance.save()
