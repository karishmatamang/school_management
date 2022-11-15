from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.views import status

class AttendanceCreateTest(APITestCase):
    attendance_url=reverse('attendance_create')
    attendance_url2=reverse('attendance_detail',kwargs={"pk":1})
    def setUp(self):
        self.data1={"date":"2022-09-26"}
    
    def test_create_attendance(self):
        response=self.client.post(self.attendance_url, self.data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_attendace(self):
        response=self.client.get(self.attendance_url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
class AttendanceDetailTest(APITestCase):
    attendance_url=reverse('attendance_create')
    attendance_url1=reverse('attendance_detail',kwargs={"pk":1})
    attendance_url2=reverse('attendance_detail',kwargs={"pk":2})
    def setUp(self):
        self.data1={"date":"2022-09-26"}
        self.data2={"date":"2022-09-27"}
        self.client.post(self.attendance_url, self.data1, format='json')
        self.client.post(self.attendance_url, self.data2, format='json')

    def test_get_attendance_detail(self):
        response1=self.client.get(self.attendance_url1)
        response2=self.client.get(self.attendance_url2)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
    
    def test_put_attendance_detail(self):
        data={"date":"2022-09-28"}
        response=self.client.put(self.attendance_url2,data,fromat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_attendance_detail(self):
        response=self.client.delete(self.attendance_url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

