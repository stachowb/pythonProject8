from django.db import models
from companies.models import Company

class Driver(models.Model):
    name = models.CharField(max_length=200)
    prof_pic = models.ImageField(upload_to='drivers', default="no_pic.png")

    EQ_TYPES = (
        (1, "Containerbil"),
        (2, "Containerbil m/løftelem"),
        (3, "Trekker"),
        (4, "-")
    )
    eq_type = models.IntegerField(choices=EQ_TYPES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
