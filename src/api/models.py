from django.db import models
from uuid import uuid4

# Create your models here.

class Country(models.Model):
    
    _uuid = models.UUIDField(unique=True, editable=False, default=uuid4())
    name = models.CharField(max_length=100, null=False, blank=False)
    official_name = models.CharField(max_length=100, null=False, blank=False)
    alpha_2 = models.CharField(max_length=2, null=False, blank=False)
    alpha_3 = models.CharField(max_length=3, null=False, blank=False)
    numeric_code = models.IntegerField(max_length=3, null=False, blank=False)
    ISO_code = models.CharField(max_length=20, null=False, blank=False)
    capital = models.CharField(max_length=100, null=False, blank=False)
    official_language = models.CharField(max_length=100, null=False, blank=False)
    phone_code = models.CharField(max_length=10, null=False, blank=False)
    currency_name = models.CharField(max_length=50, null=False, blank=False)
    currency_code = models.CharField(max_length=10, null=False, blank=False)
    
    def __str__(self):
        return self.name

