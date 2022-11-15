from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.views import status

class EventCreateTest(APITestCase):
    event_url=reverse('event_create')
    event_url2=reverse('event_detail',kwargs={"pk":1})
    event_url3=reverse('event_detail',kwargs={"pk":2})
    event_url4=reverse('event_detail',kwargs={"pk":3})
    def setUp(self):
        self.event1={"title":"Sports day","description":"basketball competetion of grade 10 and 9","start_time":"2022-06-05","end_time":"2022-06-05"}
        self.event2={"title":"Sports day","description":"Football competetion of grade 10 and 9","start_time":"2022-06-06","end_time":"2022-06-06"}
        self.event3={"title":"Sports day","description":"Volleyball competetion of grade 10 and 9","start_time":"2022-06-08","end_time":"2022-06-08"}

    def test_create_event(self):
        response1=self.client.post(self.event_url, self.event1, format='json')
        response2=self.client.post(self.event_url, self.event2, format='json')
        response3=self.client.post(self.event_url, self.event3, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)
    
    def test_get_event(self):
        response=self.client.get(self.event_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class EventDetailTest(APITestCase):
    event_url=reverse('event_create')
    event_url2=reverse('event_detail',kwargs={"pk":1})
    event_url3=reverse('event_detail',kwargs={"pk":2})
    event_url4=reverse('event_detail',kwargs={"pk":3})
    def setUp(self):
        self.event1={"title":"Sports day","description":"basketball competetion of grade 10 and 9","start_time":"2022-06-05","end_time":"2022-06-05"}
        self.event2={"title":"Sports day","description":"Football competetion of grade 10 and 9","start_time":"2022-06-06","end_time":"2022-06-06"}
        self.event3={"title":"Sports day","description":"Volleyball competetion of grade 10 and 9","start_time":"2022-06-08","end_time":"2022-06-08"}
        self.client.post(self.event_url, self.event1, format='json')
        self.client.post(self.event_url, self.event2, format='json')
        self.client.post(self.event_url, self.event3, format='json')

    def test_get_event_detail(self):
        response1=self.client.get(self.event_url2)
        response2=self.client.get(self.event_url3)
        response3=self.client.get(self.event_url4)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
    
    def test_put_event_detail(self):
        event1={"title":"Sports day","description":"basketball competetion of grade (10 and 9) and (7 and 8)","start_time":"2022-06-05","end_time":"2022-06-05"}
        event2={"title":"Sports day","description":"tabletennis competetion of grade 10 and 9","start_time":"2022-06-06","end_time":"2022-06-06"}
        response1=self.client.put(self.event_url2, event1, format='json')
        response2=self.client.put(self.event_url3,event2, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_patch_event_detail(self):
        event3={"start_time":"2022-06-07","end_time":"2022-06-09"}
        response1=self.client.patch(self.event_url4, event3, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
    
    def test_delete_event_detail(self):
        response1=self.client.delete(self.event_url2)
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
        

  