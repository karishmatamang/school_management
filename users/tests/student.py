from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
from grade.models import GradeModel, Section

class StudentTest(APITestCase):
    student_url=reverse('student_create')
    def setUp(self):
        grade1=GradeModel.objects.create(grade=1)
        grade2=GradeModel.objects.create(grade=2)
        self.section1=Section.objects.create(grade=grade1,section="A")
        self.section2=Section.objects.create(grade=grade1,section="B")
        self.section3=Section.objects.create(grade=grade2,section="A")        
        self.student1={"fullname":"test student","email":"teststudent1@test.com","password":"teststudent","role":"STUDENT",
        "contact":9843804162,"address":"kathmandu","enroll_date":"2022-02-03","section_id":self.section1.id,
        "fathers_name":"father", "mothers_name":"mother","guardian_contact":9843804162,"reffered_name":"testreffered",
        "reffered_contact":9841561234,"documents":None,"profile":None,"entrance_grade":3}
        self.student2={"fullname":"test student","email":"teststudent2@test.com","password":"teststudent","role":"STUDENT",
        "contact":9843804162,"address":"jorapti","enroll_date":"2022-02-03","section_id":self.section3.id,
        "fathers_name":"father", "mothers_name":"mother","guardian_contact":9843804162,"reffered_name":"testreffered",
        "reffered_contact":9841561234,"documents":None,"profile":None,"entrance_grade":3}

    def test_create_student(self):        
        response1=self.client.post(self.student_url,self.student1,format="json")
        response2=self.client.post(self.student_url,self.student2,format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_get_student(self):
        response=self.client.get(self.student_url,format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)      

class StudnetDetail(APITestCase):
    student_url=reverse('student_create')    
    student_url1=reverse('student_detail',kwargs={"pk":1})
    student_url2=reverse('student_detail',kwargs={"pk":2})
    def setUp(self):
        grade1=GradeModel.objects.create(grade=1)
        grade2=GradeModel.objects.create(grade=2)
        self.section1=Section.objects.create(grade=grade1,section="A")
        self.section2=Section.objects.create(grade=grade1,section="B")
        self.section3=Section.objects.create(grade=grade2,section="A")
        self.student1={"fullname":"test student","email":"teststudent1@test.com","password":"teststudent","role":"STUDENT",
        "contact":9843804162,"address":"kathmandu","enroll_date":"2022-02-03","section_id":self.section1.id,
        "fathers_name":"father", "mothers_name":"mother","guardian_contact":9843804162,"reffered_name":"testreffered",
        "reffered_contact":9841561234,"documents":None,"profile":None,"entrance_grade":3}
        self.student2={"fullname":"test student","email":"teststudent2@test.com","password":"teststudent","role":"STUDENT",
        "contact":9843804162,"address":"jorapti","enroll_date":"2022-02-03","section_id":self.section3.id,
        "fathers_name":"father", "mothers_name":"mother","guardian_contact":9843804162,"reffered_name":"testreffered",
        "reffered_contact":9841561234,"documents":None,"profile":None,"entrance_grade":3}
        self.client.post(self.student_url,self.student1,format="json")
        self.client.post(self.student_url,self.student2,format="json")

    def test_get_student_detail(self):        
        response1=self.client.get(self.student_url1,format="json")
        response2=self.client.get(self.student_url2,format="json")
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_put_student_detail(self):
        self.student3={"contact":9843804162,"address":"jorpati","enroll_date":"2022-02-10","section_id":self.section1.id,
        "fathers_name":"father", "mothers_name":"mother","guardian_contact":9843804162,"reffered_name":"testreffered",
        "reffered_contact":9841561234,"documents":None,"profile":None,"entrance_grade":3}
        self.student4={"fullname":"test student","email":"teststudent2@test.com","password":"teststudent","role":"STUDENT",
        "contact":9843804162,"address":"kathmandu","enroll_date":"2022-02-03","section_id":self.section3.id,
        "fathers_name":"father", "mothers_name":"mother","guardian_contact":9843804162,"reffered_name":"testreffered",
        "reffered_contact":9841561234,"documents":None,"profile":None,"entrance_grade":3}
        response1=self.client.put(self.student_url1,self.student3,format="json")
        response2=self.client.put(self.student_url2,self.student4,format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
    
    def test_patch_student_detail(self):
        self.student5={"mothers_name":"testmother"}
        self.student6={"fathers_name":"testfather"}
        response1=self.client.patch(self.student_url1,self.student5,format="json")
        response2=self.client.patch(self.student_url2,self.student6,format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response1.data["mothers_name"],"testmother")
        self.assertEqual(response2.data["fathers_name"],"testfather")
    
    def test_delete_student_detail(self):
        response1=self.client.delete(self.student_url2,format="json")
        self.assertEqual(response1.status_code, status.HTTP_204_N)
    
