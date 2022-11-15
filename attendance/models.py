from django.db import models
from users.models import UserAccount,TeacherAccount,StaffAccount,StudentAccount


class AttendanceModel(models.Model):
    date=models.DateField(blank=True)

    def __str__(self) -> str:     
        return f'{self.date}'   

class Attendance_Student(models.Model):
    attendance_id = models.ForeignKey(AttendanceModel, on_delete=models.CASCADE)
    student_id= models.ForeignKey(StudentAccount, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return f'{self.attendance_id}'

class Attendance_Employee(models.Model):
    attendance_id = models.ForeignKey(AttendanceModel, on_delete=models.CASCADE)
    teacher_id= models.ForeignKey(TeacherAccount, on_delete=models.CASCADE, blank=True, null=True)
    staff_id= models.ForeignKey(StaffAccount, on_delete=models.CASCADE, blank=True,null=True )

    def __str__(self) -> str:
        return f'{self.attendance_id}'

