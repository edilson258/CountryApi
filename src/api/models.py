from django.db import models
from uuid import uuid4
# Create your models here.

class Country(models.Model):
    
    _id = models.UUIDField(unique=True, editable=False, default=uuid4())
    name = models.CharField(max_length=100, null=False, blank=False)
    official_name = models.CharField(max_length=100, null=False, blank=False)
    ISO_code = models.CharField(max_length=3, null=False, blank=False)
    capital = models.CharField(max_length=100, null=False, blank=False)
    language = models.CharField(max_length=100, null=False, blank=False)
    phone_code = models.CharField(max_length=10, null=False, blank=False)
    currency_name = models.CharField(max_length=50, null=False, blank=False)
    currency_code = models.CharField(max_length=10, null=False, blank=False)
    
    def __str__(self):
        return self.name

