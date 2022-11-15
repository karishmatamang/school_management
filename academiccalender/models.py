from django.db import models

# Create your models here.
class AcademicCalenderModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return self.title