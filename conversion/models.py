from __future__ import unicode_literals

from django.db import models

# Create your models here.
class save_data(models.Model):
    convert_from = models.TextField()
    convert_to = models.TextField()
    amount = models.TextField()
