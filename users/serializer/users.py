from rest_framework import serializers
from users.models import UserAccount,SchoolAccount
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from users.utils import Util
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError

class UserSignupSerializer(serializers.ModelSerializer):    
    fullname = serializers.CharField(max_length=250)
    email = serializers.EmailField(max_length=250)    
    password = serializers.CharField(max_length=250, write_only=True)

    class Meta:
        model = UserAccount
        fields = ['id', 'fullname', 'email', 'password','is_superuser','is_active', 'role',
        'is_staff','is_guest']
        
    def validate(self, args) :
        email = args.get('email', None)    
        if UserAccount.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email' : ('email already exists')})       
        return super().validate(args)

    def create(self, validated_data):
        return UserAccount.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=250)
  class Meta:
    model = UserAccount
    fields = ['email', 'password']

class LogoutSerializer(serializers.Serializer):
   refresh = serializers.CharField()
   default_error_message = {
       'bad_token': ('Token is expired or invalid')
   }
   def validate(self, attrs):
       self.token = attrs['refresh']
       return attrs
   def save(self, **kwargs):
    try:
      RefreshToken(self.token).blacklist()  
    except TokenError:
      self.fail('bad_token')

class UserChangePasswordSerializer(serializers.Serializer):
  old_password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  new_password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)

  def validate_old_password(self, value):
        user = self.context['user']
        if not user.check_password(value):
            raise serializers.ValidationError(
                ('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

class SendPasswordResetEmailSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    fields = ['email']

  def validate(self, attrs):
    email = attrs.get('email')
    if UserAccount.objects.filter(email=email).exists():
      user = UserAccount.objects.get(email = email)
      uid = urlsafe_base64_encode(force_bytes(user.id))
      print('Encoded UID', uid)
      token = PasswordResetTokenGenerator().make_token(user)
      print('Password Reset Token', token)
      link = 'http://localhost:8000/users/reset-password/'+uid+'/'+token
      print('Password Reset Link', link)
      body = 'Click Following Link to Reset Your Password '+link
      data = {
        'subject':'Reset Your Password',
        'body':body,
        'to_email':user.email
      }
      Util.send_email(data)
      return attrs
    else:
      raise serializers.ValidationError('You are not a Registered User')

class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_base64_decode(uid))
      user = UserAccount.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(user, token)
      raise serializers.ValidationError('Token is not Valid or Expired')

    

    