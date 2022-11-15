from django.urls import path
from attendance.views import (
    AttendanceCreateAndList, 
    Attendance_StudentCreateAndList,
    Attendance_StudentUpdateAndDelete,
    AttendanceUpdateAndDelete,
    Attendance_EmployeeCreateAndList,
    Attendance_EmployeeUpdateAndDelete)

urlpatterns = [
    path('',AttendanceCreateAndList.as_view(),name='attendance_create'),
    path('<int:pk>/',AttendanceUpdateAndDelete.as_view(),name='attendance_detail'),
    path('attendancestudent/',Attendance_StudentCreateAndList.as_view(), name='studentattendance_create'),
    path('attendancestudent/<int:pk>/',Attendance_StudentUpdateAndDelete.as_view(),name='studentattendance_detail'),
    path('attendanceemployee/',Attendance_EmployeeCreateAndList.as_view(), name='employeeattendance_create'),
    path('attendanceemployee/<int:pk>/',Attendance_EmployeeUpdateAndDelete.as_view(), name='employeeattendance_detail')
]
