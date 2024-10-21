from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    video = models.FileField(upload_to='projects/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')])

    def __str__(self):
        return self.title
    

