from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django_cryptography.fields import encrypt
from rest_framework_api_key.models import APIKey


class PDE(models.Model):
    pde = encrypt(models.FileField(upload_to='pde/files/', max_length=250))
    ip = models.CharField(max_length=16)
    machine = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    rank = models.FloatField(null=True, blank=True, default=None)
    filename = models.CharField(max_length=512)
    hash = encrypt(models.CharField(max_length=256, default=None, blank=True))
    # api = models.CharField(max_length=256, default="N/A", blank=True)
    api = models.ForeignKey(APIKey, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + " " + self.ip

    class Meta:
            verbose_name_plural = "PDE"
