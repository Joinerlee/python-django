from django.db import models

class Research(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    image = models.ImageField(upload_to='research/', null=True, blank=True)
    video = models.FileField(upload_to='research/', null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')])

    def __str__(self):
        return self.title