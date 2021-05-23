from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from drivers.models import Driver
from companies.models import Company


class Shift(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField()
    km_driven = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True)

    # post_save
    shift_length = models.DurationField(blank=True, null=True)
    above_200 = models.IntegerField(blank=True, null=True)
    # bonus_time = models.DurationField(blank=True, null=True)
    # regular_pay = models.FloatField(blank=True, null=True)
    # bonus_pay = models.FloatField(blank=True, null=True)
    bonus_km = models.FloatField(blank=True, null=True)
    # total = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.__str__())
        return super().save(self, *args, **kwargs)

    def __str__(self):
        return f"{self.driver}-{self.clock_in}-{self.clock_out}"

    def get_absolute_url(self):
        return reverse('shifts-list', kwargs={'slug': self.slug})