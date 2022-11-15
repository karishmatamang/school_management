from rest_framework import serializers
from users.models import TeacherAccount,Teacher

class TeacherSignupSerializer(serializers.ModelSerializer):   
 
    class Meta:
        model = TeacherAccount
        fields = ['id','user','contact','address','qualification','is_class_teacher','section_id','profile','useracc']
        depth=1     
    
    def validate(self, args) :            
        return super().validate(args)

    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)

class TeacherRegisterSerializer(serializers.ModelSerializer):   
 
    class Meta:
        model = TeacherAccount
        fields = ['id','contact','fullname','address','qualification','is_class_teacher','section_id','profile','useracc']
        depth=1    
   


