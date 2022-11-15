from urllib import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.views import status
from grade.models import GradeModel

class CourseCreateTest(APITestCase):
    course_url=reverse('course_create')
    def setUp(self):
        self.grade1=GradeModel.objects.create(grade=1)
        self.grade2=GradeModel.objects.create(grade=2)
        self.course1={"name":"english","credit_hour":"6","grade":self.grade1.id}
        self.course2={"name":"Nepali","credit_hour":"6","grade":self.grade1.id}
        self.course3={"name":"english","credit_hour":"6","grade":self.grade2.id}
    
    def test_create_course(self):
        response1=self.client.post(self.course_url,self.course1,format="json" )
        response2=self.client.post(self.course_url,self.course2,format="json" )
        response3=self.client.post(self.course_url,self.course3,format="json" )
        print (response1.data)
        self.assertEqual(response1.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code,status.HTTP_201_CREATED)
    
    def test_get_course(self):
        response=self.client.get(self.course_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class CourseDetailTest(APITestCase):
    course_url=reverse('course_create')
    course_url2=reverse('course_detail', kwargs={"pk":1})
    course_url3=reverse('course_detail', kwargs={"pk":2})
    course_url4=reverse('course_detail', kwargs={"pk":3})

    def setUp(self):
        self.grade1=GradeModel.objects.create(grade=1)
        self.grade2=GradeModel.objects.create(grade=2)
        self.course1={"name":"english","credit_hour":"6","grade":self.grade1.id}
        self.course2={"name":"Nepali","credit_hour":"6","grade":self.grade1.id}
        self.course3={"name":"english","credit_hour":"6","grade":self.grade2.id}
        self.client.post(self.course_url,self.course1,format="json" )
        self.client.post(self.course_url,self.course2,format="json" )
        self.client.post(self.course_url,self.course3,format="json" )        

    def test_get_detail_course(self):
        response1=self.client.get(self.course_url2)
        response2=self.client.get(self.course_url3)
        response3=self.client.get(self.course_url4)
        self.assertEqual(response1.status_code,status.HTTP_200_OK)
        self.assertEqual(response2.status_code,status.HTTP_200_OK)
        self.assertEqual(response3.status_code,status.HTTP_200_OK)
    
    def test_put_detail_course(self):
        course1={"name":"Nepali","credit_hour":"6","grade":self.grade1.id}
        course2={"name":"Social","credit_hour":"6","grade":self.grade2.id}
        response1=self.client.put(self.course_url2,course1,format="json" )
        response2=self.client.put(self.course_url2,course2,format="json" )
        self.assertEqual(response1.status_code,status.HTTP_200_OK)
        self.assertEqual(response2.status_code,status.HTTP_200_OK)
    
    def test_patch_detail_course(self):
        course1={"name":"Math"}
        response1=self.client.patch(self.course_url2,course1,format="json" )
        self.assertEqual(response1.status_code,status.HTTP_200_OK)

    def test_delete_detail_course(self):
        response1=self.client.delete(self.course_url4)
        self.assertEqual(response1.status_code,status.HTTP_204_NO_CONTENT)
    
   

