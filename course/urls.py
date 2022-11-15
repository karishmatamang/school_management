from django.urls import path
from course.views import CourseCreateAndList, CourseUpdateAndDetail

urlpatterns = [
    path('',CourseCreateAndList.as_view(),name='course_create'),
    path('<int:pk>/',CourseUpdateAndDetail.as_view(),name='course_detail'),
]
