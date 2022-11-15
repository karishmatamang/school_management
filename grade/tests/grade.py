from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.views import status
from grade.models import GradeModel

class TestGradeCreate(APITestCase):
    grade_url=reverse('grade_create')
    def setUp(self):
        self.grade1={"grade":1}
        self.grade2={"grade":2}
    def test_grade_create(self):
        response1=self.client.post(self.grade_url,self.grade1, format="json")
        response2=self.client.post(self.grade_url,self.grade2, format="json")
        self.assertEqual(response1.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code,status.HTTP_201_CREATED)
    def test_grade_get(self):
        response1=self.client.get(self.grade_url, format="json")
        self.assertEqual(response1.status_code,status.HTTP_200_OK)
        
class TestGradeDeatil(APITestCase):
    grade_url=reverse('grade_create')
    grade_url2=reverse('grade_detail',kwargs={"pk":1})
    grade_url3=reverse('grade_detail',kwargs={"pk":2})
    def setUp(self):
        self.grade1={"grade":1}
        self.grade2={"grade":2}
        self.client.post(self.grade_url,self.grade1, format="json")
        self.client.post(self.grade_url,self.grade2, format="json")
        
    def test_grade_get_detail(self):
        response1=self.client.get(self.grade_url2, format="json")
        self.assertEqual(response1.status_code,status.HTTP_200_OK)
    
    def test_grade_put(self):
        self.grade1={"grade":3}
        response1=self.client.put(self.grade_url2, format="json")
        self.assertEqual(response1.status_code,status.HTTP_201_CREATED)
    
    def test_grade_delete(self):
        response1=self.client.put(self.grade_url2, format="json")
        self.assertEqual(response1.status_code,status.HTTP_201_CREATED)
