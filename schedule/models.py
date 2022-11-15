from pyexpat import model
from statistics import mode
from django.db import models
from course.models import CourseModel
from users.models import TeacherAccount
from grade.models import Section
from django.utils import timezone
class ScheduleModel(models.Model):
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    section=models.ForeignKey(Section, on_delete=models.CASCADE)
    course=models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    teacher=models.ForeignKey(TeacherAccount,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.course}'