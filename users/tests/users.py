from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status

# class UserTests(APITestCase):
#     def setUp(self):
#         self.url = reverse('user_create') 
#         self.data={"fullname":"testcase","email":"testcase@test.com","password":"testcase","role":"ADMIN"}
   
#     def test_create_user(self):
#         response=self.client.post(self.url,self.data,format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
#     def test_get_user(self):
#         response=self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class UserDetailTests(APITestCase): 
#     url = reverse('user_create') 
#     url2=reverse('user_detail',kwargs={"pk":1})  

#     def setUp(self):        
#         data={"fullname":"testcase","email":"testcase@test.com","password":"testcase","role":"ADMIN"}
#         self.client.post(self.url, data, format='json')       

#     def test_get_user_detail(self):
#         user=self.client.get(self.url2)
#         self.assertEqual(user.status_code, status.HTTP_200_OK)

#     def test_put_user_detail(self):
#         data={"fullname":"teststaff","email":"teststaff@test.com","password":"teststaff","role":"ADMIN"}
#         user=self.client.put(self.url2,data,format='json')
#         self.assertEqual(user.status_code, status.HTTP_200_OK)
    
#     def test_patch_user_detail(self):
#         data={"email":"testcase52@gmail.com"}
#         user=self.client.patch(self.url2,data,format='json')
#         self.assertEqual(user.status_code, status.HTTP_200_OK)
    
#     def test_delete_user_detail(self):
#         user=self.client.delete(self.url2)
#         self.assertEqual(user.status_code, status.HTTP_204_NO_CONTENT)

class UserLoginTest(APITestCase):
    url = reverse('user_create') 
    login=reverse('login')
    def setUp(self):        
        data={"fullname":"testcase","email":"testcase52@test.com","password":"testcase","role":"ADMIN"}
        self.client.post(self.url, data, format='json') 

    def test_login_user(self):
        data1={"email":"testcase52@test.com","password":"testcase"}
        data2={"email":"testcase5@test.com","password":"testcase"}
        data3={"email":"testcase52@test.com","password":"testca"}
        response1=self.client.post(self.login, data1, format='json')
        response2=self.client.post(self.login, data2, format='json')
        response3=self.client.post(self.login, data3, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
    
    

    

    


            