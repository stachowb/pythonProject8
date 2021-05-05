from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, blank=True)
    owner = models.CharField(max_length=60)

    def __str__(self):
        return str(self.company_name)