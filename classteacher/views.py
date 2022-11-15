from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from classteacher.models import ClassTeacherModel
from classteacher.serializer import ClassTeacherSerializer
from grade.models import Section
from users.models import TeacherAccount
from django.utils.decorators import method_decorator
from users.decorators import role_required

class ClassteacherListAndCreate(APIView):
    def get(self, request):
        classteacher=ClassTeacherModel.objects.all()
        serializer=ClassTeacherSerializer(classteacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def post(self, request):
        data=request.data
        serializer=ClassTeacherSerializer(data=request.data)
        if serializer.is_valid():
            teacher=TeacherAccount.objects.filter(pk=request.data['teacher_id']).get()
            section=Section.objects.filter(pk=request.data['section_id']).get()
            print (teacher.is_class_teacher)
            if teacher.is_class_teacher==True:
                try:
                    classteacher=ClassTeacherModel.objects.filter(teacher_id=teacher.id).get()
                    return Response("the class teacher has been alreaady assigned or the given section already has class teacher")
                except:
                    classteacher=ClassTeacherModel.objects.create(teacher_id=teacher,section_id=section)
                    classteacher.save()                                        
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("the given teacher is not authorized to become class teacher",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class ClassTeacherUpdateAndDelete(APIView):
    def get(self, request, pk):
        classteacher=ClassTeacherModel.objects.get(pk=pk)
        serializer=ClassTeacherSerializer(classteacher, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def put(self, request,pk):
        classteacher=ClassTeacherModel.objects.get(pk=pk)
        serializer=ClassTeacherSerializer(classteacher, data=request.data)
        if serializer.is_valid():
            teacher=TeacherAccount.objects.filter(pk=request.data['teacher_id']).get()
            section=Section.objects.filter(pk=request.data['section_id']).get()
            if teacher.is_class_teacher==True:
                try:
                    classteacher=ClassTeacherModel.objects.filter(teacher_id=teacher.id).get()
                    return Response("the class teacher has been alreaady assigned or the given section already has class teacher")
                except:
                    classteacher=ClassTeacherModel.objects.create(teacher_id=teacher,section_id=section)
                    classteacher.save()                                        
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("the given teacher is not authorized to become class teacher",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def patch(self, request, pk):
        classteacher=ClassTeacherModel.objects.get(pk=pk)
        serializer=ClassTeacherSerializer(classteacher, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                section=Section.objects.filter(pk=request.data['section_id']).get()
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK )
            except:
                teacher=TeacherAccount.objects.filter(pk=request.data['teacher_id']).get()                
                if teacher.is_class_teacher==True:
                    try:
                        classteacher=ClassTeacherModel.objects.filter(teacher_id=teacher.id).get()
                        return Response("the class teacher has been alreaady assigned or the given section already has class teacher")
                    except:
                        serializer.save()                                      
                        return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response("the given teacher is not authorized to become class teacher",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN','TEACHER'],),name='dispatch')
    def delete(self, request, pk):
        classteacher=ClassTeacherModel.objects.get(pk=pk)
        classteacher.delete()
        return Response("the given class-techer of given section has been delete",status=status.HTTP_204_NO_CONTENT)

