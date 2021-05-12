from django.db import models
from drivers.models import Driver
from companies.models import Company
from datetime import timedelta


class Shift(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(blank=True)
    clock_out = models.DateTimeField(blank=True)
    km_driven = models.IntegerField(default=0)

    shift_length = models.DurationField(blank=True, null=True, default=timedelta(0))
    above_200 = models.IntegerField(blank=True, null=True)

    # bonus_time = models.DurationField()
    # regular_pay = models.FloatField()
    # bonus_pay = models.FloatField()
    # bonus_km = models.FloatField()
    # total = models.FloatField()

    def __str__(self):
        return f"{self.driver} -- {self.clock_in} - {self.clock_out}"
