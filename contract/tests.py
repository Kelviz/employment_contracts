from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import EmploymentAgreement
from .serializers import EmploymentAgreementSerializers


class EmploymentAgreementListCreateTests(TestCase):
        def setUp(self):
                self.client = Client()
                self.signup_url = reverse('signup')
                self.list_create_url = reverse('employment-agreements')

                self.valid_payload = {
                        "employee_name": "John Doe",
                        "role": "Developer",
                        "start_date": "2024-07-01",
                        "end_date": "2025-06-30",
                        "salary": 80000,
                        "terms": "Full-time, benefits included",
                        "other_details": {"department": "Engineering", "manager": "Jane Smith"}
                }

                self.invalid_payload = {
                        "employee_name": "John Doe",
                        "start_date": "",
                        "end_date": "2025-06-30",
                        "salary": '',
                        "terms": "Full-time, benefits included",
                        "other_details": {"department": "Engineering", "manager": "Jane Smith"}
                }

                self.user = User.objects.create_user(username='testuser', password='testpassword')
                self.token, created = Token.objects.get_or_create(user=self.user)
                self.auth_headers = {'HTTP_AUTHORIZATION': 'Token ' + self.token.key}

                EmploymentAgreement.objects.create(
                        employee_name = "John Doe",
                        role = "Developer",
                        start_date = "2024-07-01",
                        end_date = "2025-06-30",
                        salary = 80000,
                        terms = "Full-time, benefits included",
                        other_details = {"department": "Engineering", "manager": "Jane Smith"}
                        )
                
                EmploymentAgreement.objects.create(
                        employee_name='Jane Smith',
                        role='Designer',
                        salary=55000,
                        start_date="2024-07-01",
                        end_date="2025-07-01",
                        terms = "Full-time, benefits included",
                        other_details = {"department": "Engineering", "manager": "Jane Smith"}
                        )


        def test_get_employment_agreement(self):
                #Test to list all employment agreements
                response = self.client.get(self.list_create_url, **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)

                agreements = EmploymentAgreement.objects.all()
                serializer = EmploymentAgreementSerializers(agreements, many=True)
                self.assertEqual(response.data, serializer.data)

        
        def test_create_valid_employment_agreement(self):
                #Test to create a valid employment agreement
                response = self.client.post(
                        self.list_create_url,
                        **self.auth_headers,
                        data = self.valid_payload,
                        content_type = "application/json"
                )

                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(EmploymentAgreement.objects.count(), 3)


        def test_create_invalid_employment_agreement(self):
                #Test to create a invalid employment agreement
                response = self.client.post(
                        self.list_create_url,
                        **self.auth_headers,
                        data = self.invalid_payload,
                        content_type="application/json"
                )

                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(EmploymentAgreement.objects.count(), 2)


        def test_partial_update_employment_agreement(self):
                agreement = EmploymentAgreement.objects.first()

                partial_payload = {
                        "salary": '340000',
                }

                response = self.client.patch(
                        f"{self.list_create_url}{agreement.id}/",
                        **self.auth_headers,
                        data=partial_payload,
                        content_type='application/json'
                        )
                
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                agreement.refresh_from_db()
                self.assertEqual(agreement.salary, 340000)


        def test_delete_employment_agreement(self):
                agreement = EmploymentAgreement.objects.first()
                response = self.client.delete(
                f"{self.list_create_url}{agreement.id}/",
                **self.auth_headers
                )
                self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
                self.assertEqual(EmploymentAgreement.objects.count(), 1)


        def test_search_by_employee_name(self):
                url = reverse('employment-agreement-search')
                response = self.client.get(url, {'employee_name': 'John'},  **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 1)
                self.assertEqual(response.data[0]['employee_name'], 'John Doe')

        def test_search_by_role(self):
                url = reverse('employment-agreement-search')
                response = self.client.get(url, {'role': 'Developer'}, **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 1)
                self.assertEqual(response.data[0]['role'], 'Developer')


        def test_search_by_salary_range(self):
                url = reverse('employment-agreement-search')
                response = self.client.get(url, {'salary_min': 50000, 'salary_max': 80000},  **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 2)

        def test_search_by_start_date(self):
                url = reverse('employment-agreement-search')
                response = self.client.get(url, {'start_date': '2024-01-01'}, **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 2)

     

        def test_search_by_end_date(self):
                url = reverse('employment-agreement-search')
                response = self.client.get(url, {'end_date': '2025-07-01'},  **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 2)
                self.assertEqual(response.data[1]['end_date'], '2025-07-01')

        def test_combined_search_criteria(self):
                url = reverse('employment-agreement-search')
                response = self.client.get(url, {
                'employee_name': 'John',
                'role': 'Developer',
                'salary_min': 50000,
                'salary_max': 80000,
                'start_date': '2024-07-01',
                'end_date': '2025-06-30'
                },  **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 1)
                self.assertEqual(response.data[0]['employee_name'], 'John Doe')

                 

        def test_invalid_date_format(self):
                url = reverse('employment-agreement-search')
                response = self.client.get(url, {'start_date': '01-01-2023'}, **self.auth_headers)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertIn('start_date', response.data)
                self.assertEqual(response.data['start_date'], "Incorrect date format, should be YYYY-MM-DD")

         
        def test_signup_valid_payload(self):
                

                valid_payload = {
                'username': 'testuser1',
                'password': 'password1234',
                'email': 'testuser1@example.com'
        
                }

                response = self.client.post(
                        self.signup_url,
                        data= valid_payload,
                        format='json'
                )
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertIn('token', response.data)
                self.assertIn('user', response.data)


        def test_signup_invalid_payload(self):

                invalid_payload = {
                'username': '',
                'password': 'password1234',
                'email': 'testuser1.com'
        
                }

                response = self.client.post(
                        self.signup_url,
                        data= invalid_payload,
                        format='json'
                )
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


        def test_login_valid_credentials(self):
                login_url = reverse('login')

                valid_payload = {
                'username': 'testuser',
                'password': 'testpassword'
                }

                response = self.client.post(
                login_url,
                data= valid_payload,
                format='json'
                )

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIn('token', response.data)
                self.assertIn('user', response.data)

        
        def test_login_invalid_credentials(self):
                login_url = reverse('login')

                invalid_payload = {
                'username': 'testuser',
                'password': 'testpassword1222'
                }

                response = self.client.post(
                login_url,
                data= invalid_payload,
                format='json'
                )

                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
