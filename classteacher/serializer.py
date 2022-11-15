from dataclasses import field
from msilib.schema import Class
from rest_framework import serializers
from classteacher.models import ClassTeacherModel

class ClassTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassTeacherModel
        fields=['id','teacher_id','section_id']
    