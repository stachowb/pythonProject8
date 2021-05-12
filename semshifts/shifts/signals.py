from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Shift
from datetime import timedelta, datetime, time

rates = {
    "Trekker": 522,
    "Containerbil m/løftelem": 537,
    "Containerbil": 537,
    "-": 537,
    "XV71109": 600
}
# when do we start to count the bonus hours, when do we start to count break, how long is the break
morning_limit = time(hour=6, minute=0)
evening_limit = time(hour=21, minute=0)
before_break = timedelta(hours=8, minutes=0)
break_time = timedelta(hours=0, minutes=30)


def get_bonus_time(instance):
    frt = '%d-%m-%Y %H:%M'
    shift = []
    bonus_time = timedelta(0)
    start = 0
    end = 1

    clock_in = datetime.strptime(instance.clock_in, frt)
    clock_out = datetime.strptime(instance.clock_out, frt)

    # splitting shift into one-day span shifts
    shift.append([clock_in, clock_out])
    for date in shift:
        if date[start].date() != date[end].date():
            shift.append([date[start], instance.end_day(date[start])])
            shift.append([instance.start_day(date[end]), date[end]])
            shift.pop(0)

    for date in shift:
        if instance.is_weekend(date[start]):
            bonus_time += date[end] - date[start]
        else:
            # morning limit
            if date[start] < instance.bonus_limit(date[start], morning_limit) <= date[end]:
                bonus_time += instance.bonus_limit(date[start], morning_limit) - date[start]

            if date[start] < instance.bonus_limit(date[start], morning_limit) > date[end]:
                bonus_time += date[end] - date[start]

            # evening limit
            if date[end] > instance.bonus_limit(date[end], evening_limit):
                bonus_time += date[end] - instance.bonus_limit(date[end], evening_limit)

            if date[end] > instance.bonus_limit(date[end], evening_limit) < date[start]:
                bonus_time += date[end] - date[start]

    if bonus_time > before_break:
        bonus_time -= break_time

    return bonus_time


@receiver(post_save, sender=Shift)
def post_save_calc_wages(sender, instance, created, **kwargs):
    if created:
        instance.above_200 = instance.km_driven - 200 if instance.km_driven > 200 else 0
        instance.shift_length = instance.clock_out - instance.clock_in
        instance.bonus_km = 7 * instance.above_200
        instance.regular_pay = rates[instance.reg_number] * (
            instance.shift_length.total_seconds() / 3600) if instance.reg_number in rates else \
            rates[instance.driver.get_eq_type_display()] * (instance.shift_length.total_seconds() / 3600)
        instance.save()
