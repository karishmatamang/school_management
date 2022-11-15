from rest_framework import serializers
from schedule.models import ScheduleModel

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model= ScheduleModel
        fields=[
            'id',
            'start_time',
            'end_time',
            'section',
            'course',
            'teacher'
        ]