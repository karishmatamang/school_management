from rest_framework import serializers
from users.models import StaffAccount

class StaffSignupSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = StaffAccount
        fields = ('id','user','contact','address','profile','useracc')
    
    def validate(self, args) :  
        return super().validate(args)
        
    def create(self, validated_data):
        return StaffAccount.objects.create_user(**validated_data)

class StaffRegisterSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = StaffAccount
        fields = ('id','fullname','contact','address','profile','useracc')

