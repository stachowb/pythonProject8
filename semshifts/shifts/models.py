from django.db import models
from drivers.models import Driver
from companies.models import Company


class Shift(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(blank=True)
    clock_out = models.DateTimeField(blank=True)
    km_driven = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.driver} -- {self.clock_in} - {self.clock_out}"