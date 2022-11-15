from rest_framework import serializers
from users.models import StudentAccount,Student, StudentDocument


class StudentSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAccount
        fields = ('id','contact','address','section_id','enroll_date','fathers_name',
        'mothers_name','guardian_contact','reffered_name','reffered_contact','entrance_grade','profile','useracc')
        # depth=1

    def validate(self, args) :    
        return super().validate(args)

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {k: v for k, v in data.items() if v is not None}

class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAccount
        fields = ('id','fullname','contact','address','section_id','enroll_date','fathers_name',
        'mothers_name','guardian_contact','reffered_name','reffered_contact','entrance_grade','profile','useracc')

class StudentDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDocument
        fields=[
            'id',
            'student',
            'documents'
        ]
        
    