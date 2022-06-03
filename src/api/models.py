from django.db import models

class Country(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    capital = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    language = models.CharField(max_length=100, null=False, blank=False)
    currency_name = models.CharField(max_length=100, null=False, blank=False)
    currency_code = models.CharField(max_length=10, null=False, blank=False)
    alpha_2 = models.CharField(max_length=3, null=False, blank=False)
    alpha_3 = models.CharField(max_length=4, null=False, blank=False)
    numeric_code = models.CharField(max_length=5, null=False, blank=False)
    continent = models.CharField(max_length=20, null=False, blank=False)
    continent_code = models.CharField(max_length=5, null=False, blank=False)
    latitude = models.CharField(max_length=20, null=False, blank=False)
    longitude = models.CharField(max_length=20, null=False, blank=False)
    
    def __str__(self):
        return self.name
