from django.contrib import admin

from users.models import StaffAccount
from users.models import StudentAccount
from users.models import UserAccount
from users.models import TeacherAccount


# Register your models here.

admin.site.register(UserAccount)
admin.site.register(StaffAccount)
admin.site.register(TeacherAccount)
admin.site.register(StudentAccount)