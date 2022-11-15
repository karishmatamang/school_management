from django.db import models
from grade.models import GradeModel,Section
from users.models import TeacherAccount

class ClassTeacherModel(models.Model):
    teacher_id=models.ForeignKey(TeacherAccount, on_delete=models.CASCADE)
    section_id=models.OneToOneField(Section,  on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_id