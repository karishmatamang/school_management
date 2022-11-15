from http import server
import imp
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from grade.models import Section
from users.serializer.users import UserSignupSerializer,UserLoginSerializer,LogoutSerializer,UserChangePasswordSerializer,UserPasswordResetSerializer,SendPasswordResetEmailSerializer
from users.serializer.staff import StaffSignupSerializer,StaffRegisterSerializer
from users.serializer.teacher import TeacherSignupSerializer,TeacherRegisterSerializer
from users.serializer.student import StudentSignupSerializer, StudentDocumentSerializer,StudentRegisterSerializer
from users.models import SchoolAccount, UserAccount
from users.models import StaffAccount
from users.models import TeacherAccount
from users.models import StudentAccount, StudentDocument
from django.utils.decorators import method_decorator
from users.decorators import role_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserSignupAPIView(APIView):    
    def get(self,request):
        signup=UserAccount.objects.all()
        serializer=UserSignupSerializer(signup,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({"message" : "User created!!!",'token':token, "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
  def post(self, request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':"logged out successfully"},status=status.HTTP_204_NO_CONTENT,)

class UserChangePasswordView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request,*args, **kwargs):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)        
        password = request.data['new_password']
        useraccount = UserAccount.objects.get(id=request.user.id)
        password=useraccount.set_password(password)
        useraccount.save()
        UserAccount.objects.filter(id=request.user.id).update(password=useraccount.password)
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)     

class SendPasswordResetEmailView(APIView):
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
    
class UserUpdateAndDelete(APIView):
    def get(self, request,pk):
        user=UserAccount.objects.get(pk=pk)
        serializer=UserSignupSerializer(user,many=False)
        return Response (serializer.data,status=status.HTTP_200_OK)  
    
    def put(self, request,pk):
        user=UserAccount.objects.get(pk=pk)
        serializer=UserSignupSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk):
        user=UserAccount.objects.get(pk=pk)
        serializer=UserSignupSerializer(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        user=UserAccount.objects.get(pk=pk)
        user.delete()
        return Response("the data of the given user has been removed",status=status.HTTP_204_NO_CONTENT)


class StaffSignupAPIView(APIView):
    def get(self,request):
        signup=StaffAccount.objects.all()
        serializer=StaffSignupSerializer(signup,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data=request.data
        if data['useracc']=="NO":
            serializer=StaffRegisterSerializer(data=request.data)          
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "staff created!!!","staff":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
        else:
            userserializer =  UserSignupSerializer(data=request.data)
            if userserializer.is_valid():
                userserializer.save()    
                user = UserAccount.objects.last()
                staff=StaffAccount.objects.create(user= user,contact=data['contact'],address=data['address'],profile=data["profile"],useracc=data['useracc'])
                staff.save()
                serializer=StaffSignupSerializer(staff)
                return Response({"message" : "User created!!!", "user":userserializer.data,"staff":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'errors' : userserializer.errors}, status=status.HTTP_400_BAD_REQUEST)            
          

class StaffDeleteAndUpdate(APIView):
    def get(self, request,pk):
        staff=StaffAccount.objects.get(pk=pk)
        serializer=StaffSignupSerializer(staff, many=False)
        return Response (serializer.data,status=status.HTTP_200_OK)

    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def put(self, request, pk):
        staff=StaffAccount.objects.get(pk=pk)
        serializer=StaffSignupSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def patch(self, request, pk):        
        staff=StaffAccount.objects.get(pk=pk)
        serializer=StaffSignupSerializer(staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def delete(self, request,pk):
        staff=StaffAccount.objects.get(pk=pk)
        staff.delete()
        return Response ("the given staff details has been removed",status=status.HTTP_204_NO_CONTENT)


class TeacherSignupAPIView(APIView):
    def get(self,request):
        signup=TeacherAccount.objects.all()
        serializer=TeacherSignupSerializer(signup,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

    def post(self, request,*args, **kwargs):
        data=request.data
        if data['useracc']=="NO":
            serializer=TeacherRegisterSerializer(data=request.data)          
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "staff created!!!","staff":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            userserializer =  UserSignupSerializer(data=request.data)
            if userserializer.is_valid():
                userserializer.save()     
                user = UserAccount.objects.last()
                teacher=TeacherAccount.objects.create(user= user,contact=data['contact'],address=data['address'],
                qualification=data['qualification'],is_class_teacher=data['is_class_teacher'],useracc=data['useracc'],profile=data['profile'])
                teacher.save()            
                for section in data['section_id']:
                    section_obj=Section.objects.get(id=section["id"])                
                    teacher.section_id.add(section_obj)
                    serializer=TeacherSignupSerializer(teacher)
                return Response({"message" : "User created!!!", "user": userserializer.data,"teacher":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'errors' : userserializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class TeacherDeleteAndUpdate(APIView):
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def get(self,request, pk):
        teacher=TeacherAccount.objects.get(pk=pk)
        serializer=TeacherSignupSerializer(teacher,many=False)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def put(self,request,pk):
        teacher=TeacherAccount.objects.get(pk=pk)
        serializer=TeacherSignupSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def patch(self, request, pk):
        teacher=TeacherAccount.objects.get(pk=pk)
        serializer=TeacherSignupSerializer(teacher,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def delete(self, request,pk):
        teacher=TeacherAccount.objects.get(pk=pk)
        teacher.delete()
        return Response("the teacher detail of the given id has been deleted",status=status.HTTP_204_NO_CONTENT)

class StudentSignupAPIView(APIView):
    def get(self,request):
        signup=StudentAccount.objects.all()
        serializer=StudentSignupSerializer (signup,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data=request.data
        if data['useracc']=="NO":
            serializer=StudentRegisterSerializer(data=request.data)          
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "student created!!!","staff":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
        else:
            userserializer =  UserSignupSerializer(data=request.data)              
            if userserializer.is_valid():
                userserializer.save()                
                user = UserAccount.objects.last()           
                section=Section.objects.get(pk=data['section_id']) 
                student=StudentAccount.objects.create(user=user,fullname=user.fullname,contact=data['contact'],address=data['address'],enroll_date=data['enroll_date'],section_id=section,
                fathers_name=data['fathers_name'],mothers_name=data['mothers_name'],guardian_contact=data['guardian_contact'],
                reffered_name=data['reffered_name'],reffered_contact=data['reffered_contact'],entrance_grade=data['entrance_grade'],profile=data['profile'])    
                serializer=StudentSignupSerializer(student)  
                for i in data['image']:
                    student = StudentAccount.objects.last()   
                    StudentDocument.objects.create(student=student, documents=i['documents'])
                return Response({"message":"Student created!!!","user": userserializer.data,"student detail":serializer.data},status=status.HTTP_201_CREATED)
        return Response({'errors' : userserializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class StudentDocumetListAndCreate(APIView):
    def get(self, request):
        document=StudentDocument.objects.all()
        serializer=StudentDocumentSerializer (document,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)
    def post(self, request):
        serializer=StudentDocumentSerializer (data=request.data)
        if serializer.is_valid():
            student=StudentAccount.objects.filter(pk=request.data['student']).get()
            StudentDocument.objects.create(student=student, documents=request.data['documents'])
            return Response({"message":"documents has been added","document": serializer.data},status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class StudentDocuemntDetailAndDelete(APIView):
    def get(self, request, pk):
        document=StudentDocument.objects.get(pk=pk)
        serializer=StudentDocumentSerializer (document,many=False)
        return Response (serializer.data,status=status.HTTP_200_OK)
    def delete(self, request, pk):
        document=StudentDocument.objects.get(pk=pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentDeleteAndUpdate(APIView):
    def get(self, request, pk):
        student=StudentAccount.objects.get(pk=pk)
        serializer=StudentSignupSerializer (student,many=False)
        return Response (serializer.data,status=status.HTTP_200_OK)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def put(self, request, pk):
        student=StudentAccount.objects.get(pk=pk)
        serializer=StudentSignupSerializer (student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            for i in request.data['image']:
                student = StudentAccount.objects.filter(pk=student.id).get() 
                print (student)
                StudentDocument.objects.create(student=student, documents=i['documents'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def patch(self, request, pk):
        student=StudentAccount.objects.get(pk=pk)
        serializer=StudentSignupSerializer (student,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            for i in request.data['image']:
                student = StudentAccount.objects.filter(pk=student.id).get() 
                print (student)
                StudentDocument.objects.create(student=student, documents=i['documents'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER']),name='dispatch')
    def delete(self, request, pk):
        student=StudentAccount.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)