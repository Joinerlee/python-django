from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    research_field = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name