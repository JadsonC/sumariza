from django.db import models

# Create your models here.

class Sumari(models.Model):
    link = models.URLField()
    resumo = models.TextField(blank=True, null=True)