from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from grade.serializer import GradeSerializer, SectionSerializer
from grade.models import GradeModel, Section
from django.utils.decorators import method_decorator 
from users.decorators import role_required
from users.models import TeacherAccount

class GradeCreateAndList(APIView):
    def get(self,request):
        grade=GradeModel.objects.all()
        serializer=GradeSerializer(grade,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

    # @method_decorator(role_required(allowed_roles=['ADMIN','STAFF']),name='dispatch')
    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():           
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class GradeUpdateAndDelete(APIView):
    def get(self, request,pk):
        grade=GradeModel.objects.get(pk=pk)
        serializer=GradeSerializer(grade,many=False)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def put(self, request,pk):
        grade=GradeModel.objects.get(pk=pk)
        serializer=GradeSerializer(grade,data=request.data)
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def patch(self, request,pk):
        grade=GradeModel.objects.get(pk=pk)
        serializer=GradeSerializer(grade,data=request.data,partial=True)
        if serializer.is_valid():        
            serializer.save()
            return Response(data=serializer.data)
        return Response( {'errors' :serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN'],),name='dispatch')
    def delete(self, request, pk):
        grade=GradeModel.objects.get(pk=pk)
        grade.delete()
        return Response("the grade of the given id has been deleted",status=status.HTTP_204_NO_CONTENT)

class SectionCreateAndList(APIView):
    def get (self, request):
        section=Section.objects.all()
        serializer=SectionSerializer(section,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer=SectionSerializer(data=request.data)
        if serializer.is_valid():  
            try:
                grade=GradeModel.objects.filter(grade=request.data['grade']).get()
                section=Section.objects.filter(section=request.data['section']).get()
                section= Section.objects.filter(grade=grade.grade).filter(section=grade.section).get()
                return Response("the given grade and the section  has already been saved in this system")
            except:          
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SectionDetailAndDelete(APIView):
    def get(self, request, pk):
        section=Section.objects.get(pk=pk)
        serializer=SectionSerializer(section,many=False)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        section=Section.objects.get(pk=pk)
        serializer=SectionSerializer(section,data=request.data)
        if serializer.is_valid():
            try:
                grade=GradeModel.objects.filter(grade=request.data['grade']).get()
                section=Section.objects.filter(section=request.data['section']).get()
                section= Section.objects.filter(grade=grade.grade).filter(section=grade.section).get()
                return Response("the given grade and the section  has already been saved in this system")
            except:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        section=Section.objects.get(pk=pk)
        section.delete()
        return Response({"message":"The given section of this particular grade is deleted"},status=status.HTTP_204_NO_CONTENT)


