from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
from grade.models import GradeModel, Section
from users.models import Teacher, TeacherAccount

class ClassTeacherTest(APITestCase):
    classteacher_url=reverse('classteacher_create')
    def setUp(self):
        grade1=GradeModel.objects.create(grade=1)
        grade2=GradeModel.objects.create(grade=2)

        self.section1=Section.objects.create(grade=grade1,section="A")
        self.section2=Section.objects.create(grade=grade1,section="B")
        self.section3=Section.objects.create(grade=grade2,section="A")

        self.teacher1=TeacherAccount.objects.create(contact=9843804162,address="kathmandu",qualification="5 yrs of being a teacher",is_class_teacher=True)
        self.teacher1.section_id.add(self.section1.id)      
        self.teacher2=TeacherAccount.objects.create(contact=9843845678,address="jorpati",qualification="4 yrs of being a teacher",is_class_teacher=False) 
        self.teacher2.section_id.add(self.section1.id,self.section2.id) 

        self.classteacher1={"teacher_id":self.teacher1.id,"section_id":self.section1.id}
        self.classteacher2={"teacher_id":self.teacher2.id,"section_id":self.section2.id}
        

    def test_create_teacher(self):        
        response1=self.client.post(self.classteacher_url,self.classteacher1,format="json")
        response2=self.client.post(self.classteacher_url,self.classteacher2,format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_teacher(self):        
        response1=self.client.get(self.classteacher_url)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        

class ClassTeacherDetailTest(APITestCase):
    classteacher_url=reverse('classteacher_create')
    classteacher_url1=reverse('classteacher_detail',kwargs={"pk":1})
    classteacher_url2=reverse('classteacher_detail',kwargs={"pk":2})
    def setUp(self):
        grade1=GradeModel.objects.create(grade=1)
        grade2=GradeModel.objects.create(grade=2)

        self.section1=Section.objects.create(grade=grade1,section="A")
        self.section2=Section.objects.create(grade=grade1,section="B")
        self.section3=Section.objects.create(grade=grade2,section="A")

        self.teacher1=TeacherAccount.objects.create(contact=9843804162,address="kathmandu",qualification="5 yrs of being a teacher",is_class_teacher=True)
        self.teacher1.section_id.add(self.section1.id,self.section3.id)     
        self.teacher2=TeacherAccount.objects.create(contact=9843845678,address="jorpati",qualification="4 yrs of being a teacher",is_class_teacher=True) 
        self.teacher2.section_id.add(self.section1.id,self.section2.id)

        self.classteacher1={"teacher_id":self.teacher1.id,"section_id":self.section1.id} 
        self.classteacher2={"teacher_id":self.teacher2.id,"section_id":self.section2.id}       
        self.client.post(self.classteacher_url,self.classteacher1,format="json")
        self.client.post(self.classteacher_url,self.classteacher2,format="json")

    def test_get_detail(self):
        response1=self.client.get(self.classteacher_url1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
    
    def test_put_detail(self):
        classteacher1={"teacher_id":self.teacher1.id,"section_id":self.section2.id}
        classteacher2={"teacher_id":self.teacher2.id,"section_id":self.section3.id}
        response1=self.client.put(self.classteacher_url1,classteacher1,format='json')
        response2=self.client.put(self.classteacher_url1,classteacher2,format='json')
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
    
    def test_patch_detail(self):
        classteacher1={"section_id":self.section2.id}
        response1=self.client.put(self.classteacher_url1,classteacher1,format='json')
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_delete_detail(self):
        response1=self.client.delete(self.classteacher_url1)
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)

