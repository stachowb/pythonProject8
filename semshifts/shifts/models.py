from django.db import models
from drivers.models import Driver


class Shift(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField()
    km_driven = models.IntegerField(default=0)

    # post_save
    shift_length = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.driver} -- {self.clock_in} - {self.clock_out}"