from statistics import mode
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from grade.models import GradeModel, Section
from datetime import timedelta
from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken

class SchoolAccount(BaseUserManager):
    def create_superuser(self,email, fullname, password,**other_fields):               
        other_fields.setdefault('is_superuser',True),
        other_fields.setdefault('is_staff',True),
        other_fields.setdefault('is_teacher',True),    
        other_fields.setdefault('is_guest',True), 
        if other_fields.get('is_staff'):
            raise ValueError('Admin must be assigned to is_staff=True')        
        if other_fields.get('is_teacher'):
            raise ValueError('Admin must be assigned to is_teacher=True')
        if other_fields.get('is_guest'):
            raise ValueError('Admin must be assigned to is_guest=True')
        return self.create_user(email,fullname,password,**other_fields)

    def create_user(self,fullname,email,password,role,**other_fields):
        email=self.normalize_email(email)
        user=self.model(email=email,fullname=fullname,role=role,**other_fields)
        user.set_password(password)
        print (email)
        if role=="ADMIN":
            user.is_superuser=True
            user.is_staff=True
            user.is_teacher=True    
            user.is_guest=True
        if role=="GUEST":
            user.is_guest=True
            # refresh = RefreshToken.for_user(user)
            # refresh.set_exp(lifetime=datetime.timedelta(minutes=2))
            # ACCESS_TOKEN_LIFETIME: timedelta(minutes=2)
            # refresh = RefreshToken.for_user(user)
            # access_token = refresh.access_token
            # access_token.set_exp(lifetime=timedelta(minutes=2))
        user.save()  
        return user 
        

class UserAccount(AbstractBaseUser,PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "ADMIN"
        STUDENT = "STUDENT", "STUDENT"
        TEACHER = "TEACHER", "TEACHER"
        STAFF = "STAFF", "STAFF"
        GUEST="GUEST","GUEST"

    email=models.EmailField(unique=True)
    fullname = models.CharField(max_length=250)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_guest=models.BooleanField(blank=True,default=False)
    role = models.CharField(max_length=50, choices=Role.choices,default=None)
    objects=SchoolAccount()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['fullname','password']
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role
            return super().save(*args, **kwargs)
    

class TeacherManager(BaseUserManager):
    def get_queryset(self, **other_fields):
        results = super().get_queryset(**other_fields)
        return results

class Teacher(UserAccount):
    teacher = TeacherManager()
    class Meta:
        proxy = True
    def welcome(self):
        return "Only for teachers"

@receiver(post_save, sender=Teacher)
def create_user(self,instance, created, **kwargs):
    if created and instance.role == "TEACHER":        
        TeacherAccount.objects.create(user=instance)

class TeacherAccount(models.Model):
    class UserAcc(models.TextChoices):
        YES = "YES", "YES"
        NO = "NO", "NO"
    user = models.OneToOneField(UserAccount,on_delete=models.CASCADE, null=True, blank=True)
    useracc=models.CharField(max_length=50, choices=UserAcc.choices,default=None)
    fullname = models.CharField(max_length=250,null=True, blank=True)
    address = models.CharField(max_length=250)
    contact = models.BigIntegerField()
    qualification=models.CharField(max_length=250)
    section_id = models.ManyToManyField(Section)
    is_class_teacher=models.BooleanField(default=False)
    profile=models.ImageField(upload_to="upload/staff",null=True, blank=True)  


class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)

class Staff(UserAccount):
    staff= StaffManager()
    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Staff"

@receiver(post_save, sender=Staff)
def create_user(self,sender, instance, created, **kwargs):
    if created and instance.role == "STAFF":
        StaffAccount.objects.create(user=instance)

class StaffAccount(models.Model):
    class UserAcc(models.TextChoices):
        YES = "YES", "YES"
        NO = "NO", "NO"

    user = models.OneToOneField(UserAccount,on_delete=models.CASCADE,null=True,blank=True)
    fullname = models.CharField(max_length=250,null=True, blank=True)
    address = models.CharField(max_length=250)
    useracc=models.CharField(max_length=50, choices=UserAcc.choices,default=None)
    contact = models.BigIntegerField()
    profile=models.ImageField(upload_to="upload/staff",null=True, blank=True) 


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)

class Student(UserAccount):
    objects = StudentManager()
    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"

class StudentAccount(models.Model):
    class UserAcc(models.TextChoices):
        YES = "YES", "YES"
        NO = "NO", "NO"

    useracc=models.CharField(max_length=50, choices=UserAcc.choices,null=True, blank=True)
    fullname = models.CharField(max_length=250,null=True, blank=True)
    user = models.OneToOneField(UserAccount,on_delete=models.CASCADE,null=True, blank=True)  
    address = models.CharField(max_length=250)
    contact = models.BigIntegerField(null=True,blank=True)
    section_id = models.ForeignKey (Section, on_delete=models.CASCADE, blank=True, null=True)
    profile=models.ImageField(upload_to="upload/profile",null=True, blank=True)
    enroll_date=models.DateField(auto_now=False,auto_now_add=False, null=True,blank=True)
    fathers_name=models.CharField(max_length=250,null=True,blank=True)
    mothers_name=models.CharField(max_length=250,null=True,blank=True)
    guardian_contact=models.BigIntegerField(null=True,blank=True)
    reffered_name=models.CharField(max_length=250,blank=True,null=True)
    reffered_contact=models.BigIntegerField(blank=True,null=True)    
    entrance_grade=models.FloatField(null=True,blank=True)   


@receiver(post_save, sender=Student)
def create_user(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentAccount.objects.create(user=instance)

class StudentDocument(models.Model):
    student=models.ForeignKey(StudentAccount, on_delete=models.CASCADE, null= True, blank=True)
    documents=models.ImageField(upload_to="upload/student/documents", null=True, blank=True)

    def __str__(self):
        return self.student