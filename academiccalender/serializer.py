from rest_framework import serializers
from academiccalender.models import AcademicCalenderModel

class AcademicCalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model=AcademicCalenderModel
        fields=('id','title','description','start_time','end_time')