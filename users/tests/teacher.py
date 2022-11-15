from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
from grade.models import GradeModel, Section

class TeacherTest(APITestCase):
    teacher_url=reverse('teacher_create')
    section_url=reverse('section_create')
    def setUp(self):
        grade1=GradeModel.objects.create(grade=1)
        grade2=GradeModel.objects.create(grade=2)
        self.section1=Section.objects.create(grade=grade1,section="A")
        self.section2=Section.objects.create(grade=grade1,section="B")
        self.section1=Section.objects.create(grade=grade2,section="A")
        self.teacher1={"fullname":"testcase","email":"testteacher50@test.com","password":"testteacher","role":"TEACHER","contact":9843804162,
        "address":"kathmandu","qualification":"5 yrs of being a teacher","section_id":[{"id":self.section1.id}],"is_class_teacher":True}
        self.teacher2={"fullname":"testcase","email":"testteacher51@test.com","password":"testteacher","role":"TEACHER","contact":9843804162,
        "address":"kathmandu","qualification":"5 yrs of being a teacher","section_id":[{"id":self.section1.id}],"is_class_teacher":False} 

    def test_create_teacher(self):        
        response1=self.client.post(self.teacher_url,self.teacher1,format="json")
        response2=self.client.post(self.teacher_url,self.teacher2,format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_get_teacher(self):
        response=self.client.get(self.teacher_url,format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeacherDetailTest(APITestCase):
    teacher_url=reverse("teacher_create") 
    teacher_url1=reverse('teacher_detail',kwargs={"pk":1})
    teacher_url2=reverse('teacher_detail',kwargs={"pk":2})
    def setUp(self):
        grade1=GradeModel.objects.create(grade=1)
        grade2=GradeModel.objects.create(grade=2)
        self.section1=Section.objects.create(grade=grade1,section="A")
        self.section2=Section.objects.create(grade=grade1,section="B")
        self.section3=Section.objects.create(grade=grade2,section="A")
        self.teacher1={"fullname":"testcase","email":"testteacher@test.com","password":"testteacher","role":"TEACHER","contact":9843804162,
        "address":"kathmandu","qualification":"5 yrs of being a teacher","section_id":[{"id":self.section1.id}],"is_class_teacher":True}
        self.teacher2={"fullname":"testcase","email":"testteacher2@test.com","password":"testteacher","role":"TEACHER","contact":9843804162,
        "address":"kathmandu","qualification":"5 yrs of being a teacher","section_id":[{"id":self.section2.id}],"is_class_teacher":False} 
        self.client.post(self.teacher_url,self.teacher1,format="json")
        self.client.post(self.teacher_url,self.teacher2,format="json")
    
    def test_get_teacher_detail(self):        
        response1=self.client.get(self.teacher_url1)
        response2=self.client.get(self.teacher_url2)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
    
    def test_put_teacher_detail(self):
        teacher1={"contact":9843804162,"address":"kathmandu,Jorpati","qualification":"3 yrs of being a teacher","section_id":[{"id":self.section1.id}],"is_class_teacher":True}
        response1=self.client.put(self.teacher_url1,teacher1, fromat='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
    
    def test_patch_teacher_detail(self):
        teacher1={"contact":9843825235,"section_id":[{"id":self.section3.id,"id":self.section2.id}]}
        response1=self.client.patch(self.teacher_url1,teacher1, fromat='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_delete_teacher_detail(self):
        response1=self.client.delete(self.teacher_url1)
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
