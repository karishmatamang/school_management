from django.urls import path
from users.serializer.users import UserLoginSerializer
from users.views import (
     StaffDeleteAndUpdate, UserLoginView, UserSignupAPIView,UserUpdateAndDelete,
     StaffSignupAPIView, 
     TeacherSignupAPIView,TeacherDeleteAndUpdate,
     StudentSignupAPIView,StudentDeleteAndUpdate,
     UserLoginView,UserChangePasswordView,UserPasswordResetView,SendPasswordResetEmailView,
     LogoutView,StudentDocumetListAndCreate, StudentDocuemntDetailAndDelete
     )
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

urlpatterns = [
    path('',UserSignupAPIView.as_view(),name='user_create'),
    path('<int:pk>/',UserUpdateAndDelete.as_view(),name='user_detail'),
    path('staff/',StaffSignupAPIView.as_view(),name='staff_create'),
    path('staff/<int:pk>/',StaffDeleteAndUpdate.as_view(),name='staff_detail'),
    path('teacher/',TeacherSignupAPIView.as_view(),name='teacher_create'),
    path('teacher/<int:pk>/',TeacherDeleteAndUpdate.as_view(),name='teacher_detail'),
    path('student/',StudentSignupAPIView.as_view(),name='student_create'),
    path('student/<int:pk>/',StudentDeleteAndUpdate.as_view(),name='student_detail'),
    path('student/document/',StudentDocumetListAndCreate.as_view(),name='student_docuement'),
    path('student/document/<int:pk>/',StudentDocuemntDetailAndDelete.as_view(),name='student_docuement_detail'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('token/login/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())
]
