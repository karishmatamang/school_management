from rest_framework import serializers
from attendance.models import AttendanceModel, Attendance_Student,Attendance_Employee


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AttendanceModel
        fields=('id','date')


class Attendance_StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance_Student
        fields=('id','attendance_id','student_id')


class Attendance_EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance_Employee
        fields=('id','attendance_id','teacher_id','staff_id')




