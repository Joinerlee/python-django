from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200)
    doi = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    date = models.DateField()

