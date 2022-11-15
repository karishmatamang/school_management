from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status

class StaffTest(APITestCase):
    staff_url=reverse('staff_create')
    staff_url2=reverse('staff_detail',kwargs={"pk":1})

    def setUp(self):
        self.staff={"fullname":"testcase","email":"testcase@test.com","password":"testcase","role":"STAFF","contact":9843804162,"address":"jorpati"}
                
    def test_create_staff(self):        
        response=self.client.post(self.staff_url,self.staff,format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_staff(self):
        response=self.client.get(self.staff_url,format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class StaffDetailTest(APITestCase):
    staff_url=reverse("staff_create") 
    staff_url2=reverse('staff_detail',kwargs={"pk":1})
    def setUp(self):
        staff={"fullname":"testcase","email":"testcase@test.com","password":"testcase","role":"STAFF","contact":9843804162,"address":"jorpati"}       
        self.client.post(self.staff_url,staff,format="json")
    
    def test_get_staff_detail(self):
        response=self.client.get(self.staff_url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_put_detail(self):
        staff={"contact":9843804163,"address":"baneshwor"}       
        response=self.client.put(self.staff_url2,staff,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_patch_detail(self):
        staff={"address":"bagbazar"}       
        response=self.client.patch(self.staff_url2,staff,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_detail(self):
        response=self.client.delete(self.staff_url2)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    