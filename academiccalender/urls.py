from django.urls import path
from academiccalender.views import EventCreateAndList,EventUpdateAndDelete

urlpatterns = [
    path('',EventCreateAndList.as_view(),name='event_create'),
    path('<int:pk>/',EventUpdateAndDelete.as_view(),name='event_detail')
]
