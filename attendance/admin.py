from tkinter import S
from django.contrib import admin
from attendance.models import AttendanceModel,Attendance_Student

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['id','date']
admin.site.register(AttendanceModel,AttendanceAdmin)

class Student_AttendanceAdmin(admin.ModelAdmin):
    list_display=['id','attendance_id','student_id']
admin.site.register(Attendance_Student,Student_AttendanceAdmin)