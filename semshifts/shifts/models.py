from django.db import models
from drivers.models import Driver


class Shift(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    clock_in = models.CharField(max_length=50)
    clock_out = models.CharField(max_length=50)
    km_driven = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.driver} -- {self.clock_in} - {self.clock_out}"