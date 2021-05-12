from django.db import models
from drivers.models import Driver
from companies.models import Company

class Shift(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField()
    km_driven = models.IntegerField(default=0)

    # post_save
    shift_length = models.DurationField(blank=True, null=True)
    above_200 = models.IntegerField(blank=True, null=True)
    bonus_time = models.DurationField(blank=True, null=True)
    regular_pay = models.FloatField(blank=True, null=True)
    bonus_pay = models.FloatField(blank=True, null=True)
    bonus_km = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.driver} -- {self.clock_in} - {self.clock_out}"
