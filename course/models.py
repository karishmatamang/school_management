from django.db import models
from grade.models import GradeModel

class CourseModel(models.Model):
    name=models.CharField(max_length=250)
    credit_hour = models.IntegerField(blank=True, null=True)
    grade=models.ForeignKey(GradeModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name