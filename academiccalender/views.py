from academiccalender.models import AcademicCalenderModel
from academiccalender.serializer import AcademicCalenderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator 
from users.decorators import role_required


class EventCreateAndList(APIView):
    def get(self,request):
        event=AcademicCalenderModel.objects.all()
        serializer=AcademicCalenderSerializer(event,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # @method_decorator(role_required(allowed_roles=['ADMIN']),name='dispatch')
    def post(self,request):
        serializer=AcademicCalenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EventUpdateAndDelete(APIView):
    def get(self,request,pk):
        event=AcademicCalenderModel.objects.get(pk=pk)
        serializer=AcademicCalenderSerializer(event,many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # @method_decorator(role_required(allowed_roles=['ADMIN']),name='dispatch')
    def put(self,request,pk):
        event=AcademicCalenderModel.objects.get(pk=pk)
        serializer=AcademicCalenderSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN']),name='dispatch')   
    def patch(self, request, pk):
        event=AcademicCalenderModel.objects.get(pk=pk)
        serializer = AcademicCalenderSerializer(event, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response( {'errors' :serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # @method_decorator(role_required(allowed_roles=['ADMIN']),name='dispatch')
    def delete(self,request,pk):
        event=AcademicCalenderModel.objects.get(pk=pk)
        event.delete()
        return Response("event has been deleted",status=status.HTTP_204_NO_CONTENT)

        