from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    prof_pic = models.ImageField(upload_to='drivers', default="no_pic.png")
    eq_type = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
