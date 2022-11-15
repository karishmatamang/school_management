
from rest_framework import serializers
from grade.models import GradeModel, Section

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=GradeModel
        fields=['id','grade']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            'id',
            'grade',
            'section'
        ]
      
