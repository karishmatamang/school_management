from django.urls import path
from classteacher.views import ClassteacherListAndCreate, ClassTeacherUpdateAndDelete

urlpatterns = [
    path('',ClassteacherListAndCreate.as_view(),name='classteacher_create'),
    path('<int:pk>/',ClassTeacherUpdateAndDelete.as_view(),name='classteacher_detail'),
]
