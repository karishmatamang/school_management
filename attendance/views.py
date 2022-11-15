from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from attendance.models import AttendanceModel,Attendance_Student,Attendance_Employee
from attendance.serializer import AttendanceSerializer, Attendance_StudentSerializer, Attendance_EmployeeSerializer
from users.models import StudentAccount, TeacherAccount ,StaffAccount
from django.utils.decorators import method_decorator 
from users.decorators import role_required


class AttendanceCreateAndList(APIView):
    def get(self,request):
        attendance=AttendanceModel.objects.all()
        serializer=AttendanceSerializer(attendance,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def post(self,request):
        serializer=AttendanceSerializer(data=request.data)
        if serializer.is_valid():            
            try:
                attendance=AttendanceModel.objects.filter(date=request.data['date']).get()
                attend =AttendanceModel.objects.filter(date=attendance.date).get()
                return Response("the given date has already been assigned to do attendance")
            except:
                serializer.save()                
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AttendanceUpdateAndDelete(APIView):
    def get(self,request,pk):
        attendance=AttendanceModel.objects.get(pk=pk)
        serializer=AttendanceSerializer(attendance,many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def put(self, request, pk):
        attendance=AttendanceModel.objects.get(pk=pk)
        serializer=AttendanceSerializer(attendance,data=request.data)
        if serializer.is_valid():
            attendance=AttendanceModel.objects.filter(date=request.data['date']).get()
            try:
                attend = AttendanceModel.objects.filter(date=attendance.date).get()
                return Response("the given date has already been assigned to do attendance")
            except:
                serializer.save() 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')    
    def patch(self, request, pk):
        attendance=AttendanceModel.objects.get(pk=pk)
        serializer = AttendanceSerializer(attendance, data=request.data, partial=True) 
        if serializer.is_valid():
            attendance=AttendanceModel.objects.filter(date=request.data['date']).get()
            try:
                attend = AttendanceModel.objects.filter(date=attendance.date).get()
                return Response("the given date has already been assigned to do attendance")
            except:
                serializer.save() 
            return Response(data=serializer.data)
        return Response( {'errors' :serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def delete(self, request,pk):
        attendance=AttendanceModel.objects.get(pk=pk)
        attendance.delete()
        return Response("attendance of the given date has been deleted",status=status.HTTP_204_NO_CONTENT)

class Attendance_StudentCreateAndList(APIView):        
    def get(self, request):
        attendance_student=Attendance_Student.objects.all()
        serializer=Attendance_StudentSerializer(attendance_student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER']),name='dispatch')
    def post(self,request):
        serializer=Attendance_StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = StudentAccount.objects.filter(pk=request.data['student_id']).get()
            attendance=AttendanceModel.objects.filter(pk=request.data['attendance_id']).get()
            try:
                student = Attendance_Student.objects.filter(student_id=student.id).filter(attendance_id=attendance.id).get()
                return Response("attendance has been done so can't update")                
            except:
                serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)                      
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Attendance_StudentUpdateAndDelete(APIView):
    def get(self, request,pk):
        attendance_student=Attendance_Student.objects.get(pk=pk)
        serializer=Attendance_StudentSerializer(attendance_student, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def put(self, request, pk):
        attendance_student=Attendance_Student.objects.get(pk=pk)
        serializer=Attendance_StudentSerializer(attendance_student,data=request.data)
        if serializer.is_valid():
            student = StudentAccount.objects.filter(pk=request.data['student_id']).get()
            attendance=AttendanceModel.objects.filter(pk=request.data['attendance_id']).get()
            try:
                student = Attendance_Student.objects.filter(student_id=student.id).filter(attendance_id=attendance.id).get()
                return Response("attendance has been done to the given student and date so you can't update")                
            except:
                serializer.save()        
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def patch(self, request, pk):
        attendance=Attendance_Student.objects.get(pk=pk)
        serializer = Attendance_StudentSerializer(attendance, data=request.data, partial=True) 
        if serializer.is_valid():
            student = StudentAccount.objects.filter(pk=request.data['student_id']).get()
            attendance=AttendanceModel.objects.filter(pk=request.data['attendance_id']).get()
            try:
                student = Attendance_Student.objects.filter(student_id=student.id).filter(attendance_id=attendance.id).get()
                return Response("attendance has been done to the given student and date so you can't update")                
            except:
                serializer.save()
            return Response(data=serializer.data)
        return Response( {'errors' :serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def delete(self, request, pk):
        attendacne_student=Attendance_Student.objects.get(pk=pk)
        attendacne_student.delete()
        return Response("student attendance has been deleted")


class Attendance_EmployeeCreateAndList(APIView):        
    def get(self, request):
        attendance_employee=Attendance_Employee.objects.all()
        serializer=Attendance_EmployeeSerializer(attendance_employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # @method_decorator(role_required(allowed_roles=['ADMIN']),name='dispatch')
    def post(self,request):
        serializer=Attendance_EmployeeSerializer(data=request.data)
        if serializer.is_valid():            
            try:             
                attendance=AttendanceModel.objects.filter(pk=request.data['attendance_id']).get()
                try:
                    teacher = TeacherAccount.objects.filter(pk=request.data['teacher_id']).get()
                    Attendance_Employee.objects.filter(teacher_id=teacher.id).filter(attendance_id=attendance.id).get()
                    return Response("attendance of the given teacher has been done already so it can't be updated") 
                except:
                    staff = StaffAccount.objects.filter(pk=request.data['staff_id']).get()
                    Attendance_Employee.objects.filter(staff_id=staff.id).filter(attendance_id=attendance.id).get()
                    return Response("attendance of the given staff has been done already so it can't be updated")              
            except:
                serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)                      
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Attendance_EmployeeUpdateAndDelete(APIView):
    def get(self, request,pk):
        attendance_employee=Attendance_Employee.objects.get(pk=pk)
        serializer=Attendance_EmployeeSerializer(attendance_employee, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def put(self, request, pk):
        attendance_employee=Attendance_Employee.objects.get(pk=pk)
        serializer=Attendance_EmployeeSerializer(attendance_employee,data=request.data)
        if serializer.is_valid():
            try:
                attendance=AttendanceModel.objects.filter(pk=request.data['attendance_id']).get()
                try:                    
                    teacher = TeacherAccount.objects.filter(pk=request.data['teacher_id']).get()
                    Attendance_Employee.objects.filter(teacher_id=teacher.id).filter(attendance_id=attendance.id).get()
                    return Response("attendance of the given teacher has been done already so it can't be updated") 
                except:
                    staff = StaffAccount.objects.filter(pk=request.data['staff_id']).get()
                    Attendance_Employee.objects.filter(staff_id=staff.id).filter(attendance_id=attendance.id).get()
                    return Response("attendance of the given staff has been done already so it can't be updated")              
            except:
                serializer.save()   
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def patch(self, request, pk):
        attendance_employee=Attendance_Employee.objects.get(pk=pk)
        serializer = Attendance_EmployeeSerializer(attendance_employee, data=request.data, partial=True) 
        if serializer.is_valid():
            try:
                attendance=AttendanceModel.objects.filter(pk=request.data['attendance_id']).get()
                try:
                    teacher = TeacherAccount.objects.filter(pk=request.data['teacher_id']).get()
                    Attendance_Employee.objects.filter(teacher_id=teacher.id).filter(attendance_id=attendance.id).get()
                    return Response("attendance of the given teacher has been done already so it can't be updated") 
                except:
                    staff = StaffAccount.objects.filter(pk=request.data['staff_id']).get()
                    Attendance_Employee.objects.filter(staff_id=staff.id).filter(attendance_id=attendance.id).get()
                    return Response("attendance of the given staff has been done already so it can't be updated")              
            except:
                serializer.save()  
            return Response(data=serializer.data)
        return Response( {'errors' :serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def delete(self, request, pk):
        attendacne_employee=Attendance_Employee.objects.get(pk=pk)
        attendacne_employee.delete()
        return Response("student attendance has been deleted")


