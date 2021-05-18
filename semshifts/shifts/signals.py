from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Shift
from datetime import timedelta, datetime, time


@receiver(post_save, sender=Shift)
def post_save_calc_wages(sender, instance, created, **kwargs):
    if created:
        instance.above_200 = instance.km_driven - 200 if instance.km_driven > 200 else 0
        instance.shift_length = instance.clock_out - instance.clock_in
        instance.bonus_km = 7 * instance.above_200
        # instance.regular_pay = rates[instance.reg_number] * (
        #     instance.shift_length.total_seconds() / 3600) if instance.reg_number in rates else \
        #     rates[instance.driver.get_eq_type_display()] * (instance.shift_length.total_seconds() / 3600)
        instance.save()
