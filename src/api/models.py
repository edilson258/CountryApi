from django.db import models

class Country(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    alpha = models.CharField(max_length=3, null=False, blank=False)
    capital = models.CharField(max_length=255, null=False, blank=False)
    language = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    currency = models.CharField(max_length=10, null=False, blank=False)
    continent = models.CharField(max_length=255, null=False, blank=False)
    flag = models.URLField()
    
    def __str__(self):
        return self.name
