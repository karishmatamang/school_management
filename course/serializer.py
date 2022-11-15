from rest_framework import serializers
from course.models import CourseModel

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseModel
        fields=[
            'id',
            'name',
            'grade',
        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {k: v for k, v in data.items() if v is not None}