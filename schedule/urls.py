from django.urls import path
from schedule.views import ScheduleCreateAndList, ScheduleUpdateAndDelete

urlpatterns = [
    path ('',ScheduleCreateAndList.as_view()), 
    path ('<int:pk>/',ScheduleUpdateAndDelete.as_view()), 
]
