from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from schedule.models import ScheduleModel
from schedule.serializer import ScheduleSerializer
from users.models import TeacherAccount
from course.models import CourseModel
from grade.models import Section

class ScheduleCreateAndList(APIView):
    def get(self, request):
        schedule=ScheduleModel.objects.all()
        serializer=ScheduleSerializer(schedule, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data=request.data
        serializer=ScheduleSerializer(data=data)
        if serializer.is_valid():
            course=CourseModel.objects.filter(pk=data['course']).get()
            section=Section.objects.filter(pk=data['section']).get()
            teacher=TeacherAccount.objects.filter(pk=data['teacher']).get()
            if section.grade==course.grade:                                         
                try:
                    check_schedule=ScheduleModel.objects.filter(teacher=teacher.id).filter(course=course.id).filter(start_time=data['start_time']).get()
                    return Response("The teacher has been already assigned to this course for same time for other class")
                except:
                    try:
                        check_schedule=ScheduleModel.objects.filter(teacher=teacher.id).filter(start_time=data['start_time']).get()
                        return Response("The teacher has been already assigned to other class for same time")
                    except:
                        try:
                            check_schedule=ScheduleModel.objects.filter(course=course.id).filter(start_time=data['start_time']).get()
                            return Response("The teacher has been already assigned to this course for same time")
                        except:
                            serializer.save()
            else:
                return Response("the given course is not for the given section")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScheduleUpdateAndDelete(APIView):
    def get(self, request,pk):
        schedule=ScheduleModel.objects.get(pk=pk)
        serializer=ScheduleSerializer(schedule, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        data=request.data
        schedule=ScheduleModel.objects.get(pk=pk)
        serializer=ScheduleSerializer(schedule, data=data)
        if serializer.is_valid():
            course=CourseModel.objects.filter(pk=data['course']).get()
            section=Section.objects.filter(pk=data['section']).get()
            teacher=TeacherAccount.objects.filter(pk=data['teacher']).get()
            if section.grade==course.grade:                                         
                try:
                    check_schedule=ScheduleModel.objects.filter(teacher=teacher.id).filter(course=course.id).filter(start_time=data['start_time']).get()
                    return Response("The teacher has been already assigned to this course for same time for other class")
                except:
                    try:
                        check_schedule=ScheduleModel.objects.filter(teacher=teacher.id).filter(start_time=data['start_time']).get()
                        return Response("The teacher has been already assigned to other class for same time")
                    except:
                        try:
                            check_schedule=ScheduleModel.objects.filter(course=course.id).filter(start_time=data['start_time']).get()
                            return Response("The teacher has been already assigned to this course for same time")
                        except:
                            serializer.save()
            else:
                return Response("the given course is not for the given section")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        schedule=ScheduleModel.objects.get(pk=pk)
        schedule.delete()
        return Response("The given scheudel has been removed")
