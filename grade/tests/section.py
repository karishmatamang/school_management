from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.views import status
from grade.models import GradeModel

class TestSectionCreate(APITestCase):
    section_url=reverse('section_create')
    def setUp(self):
        self.grade1=GradeModel.objects.create(grade=1)
        self.grade2=GradeModel.objects.create(grade=2)
        self.section1={"grade":self.grade1.id,"section":"A"}
        self.section2={"grade":self.grade1.id,"section":"B"}
        self.section3={"grade":self.grade2.id,"section":"A"}
        self.section4={"grade":self.grade2.id,"section":"A"}
    def test_section_create(self):
        response1=self.client.post(self.section_url,self.section1, format="json")
        response2=self.client.post(self.section_url,self.section2, format="json")
        response3=self.client.post(self.section_url,self.section3, format="json")
        response4=self.client.post(self.section_url,self.section4, format="json")
        self.assertEqual(response1.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response3.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response4.status_code,status.HTTP_201_CREATED)
    
    def test_section_get_(self):
        response1=self.client.get(self.section_url,format="json")       
        self.assertEqual(response1.status_code,status.HTTP_200_OK)
       
class SectionDetailTest(APITestCase):
    section_url=reverse('section_create')    
    section_url1=reverse('section_detail',kwargs={"pk":1})
    section_url2=reverse('section_detail',kwargs={"pk":2})
    section_url3=reverse('section_detail',kwargs={"pk":3})
    def setUp(self):
        self.grade1=GradeModel.objects.create(grade=1)
        self.grade2=GradeModel.objects.create(grade=2)
        self.section1={"grade":self.grade1.id,"section":"A"}
        self.section2={"grade":self.grade1.id,"section":"B"}
        self.section3={"grade":self.grade2.id,"section":"A"}
        self.client.post(self.section_url,self.section1, format="json")
        self.client.post(self.section_url,self.section2, format="json")
        self.client.post(self.section_url,self.section3, format="json")       
        
    def test_section_get_detail(self):
        response1=self.client.get(self.section_url1,format="json")
        response2=self.client.get(self.section_url2,format="json")
        response3=self.client.get(self.section_url3,format="json")
        self.assertEqual(response1.status_code,status.HTTP_200_OK)
        self.assertEqual(response2.status_code,status.HTTP_200_OK)
        self.assertEqual(response3.status_code,status.HTTP_200_OK)
    
    def test_section_put(self):
        section1={"grade":self.grade1.id,"section":"A"}
        section2={"grade":self.grade2.id,"section":"B"}
        response1=self.client.put(self.section_url2,section1,format="json")
        response2=self.client.put(self.section_url3,section2,format="json")
        self.assertEqual(response1.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code,status.HTTP_201_CREATED)
    
    def test_section_delete(self):
        response1=self.client.delete(self.section_url2,format="json")
        self.assertEqual(response1.status_code,status.HTTP_204_NO_CONTENT)