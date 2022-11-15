from django.db import models


class GradeModel(models.Model):
    grade=models.CharField(max_length=50,unique=True)   

    def __str__ (self):
        return self.grade

class Section(models.Model):
    grade = models.ForeignKey(GradeModel, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.grade.grade)

