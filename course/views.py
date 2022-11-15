from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from course.models import CourseModel
from course.serializer import CourseSerializer

class CourseCreateAndList(APIView):
    def get(self, request):
        course=CourseModel.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CourseUpdateAndDetail(APIView):
    def get(self,request,pk):
        course=CourseModel.objects.get(pk=pk)
        serializer=CourseSerializer(course, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        course=CourseModel.objects.get(pk=pk)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        course=CourseModel.objects.get(pk=pk)
        serializer=CourseSerializer(course,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        course=CourseModel.objects.get(pk=pk) 
        course.delete()
        return Response("The course has been deleted",status=status.HTTP_204_NO_CONTENT)
