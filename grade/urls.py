from django.urls import path
from grade.views import GradeCreateAndList, GradeUpdateAndDelete, SectionCreateAndList, SectionDetailAndDelete

urlpatterns = [
    path('',GradeCreateAndList.as_view(),name='grade_create'),
    path('<int:pk>/', GradeUpdateAndDelete.as_view(),name='grade_detail'),
    path('section/',SectionCreateAndList.as_view(),name='section_create'),
    path('section/<int:pk>/',SectionDetailAndDelete.as_view(),name='section_detail'),
]