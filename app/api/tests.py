from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

User = get_user_model()


class URLTest(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='John', password='Doe')
        cls.another_user = User.objects.create_user(
            username='Jane', password='Glow')

    def setUp(self) -> None:
        self.guest_client = APIClient()
        self.user = User.objects.get(username='John')
        self.authorized_client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.authorized_client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        self.private_url = '/api/v1/users/1/'
        self.public_url = '/api/v1/users/'

    def test_list_users_unauth(self):
        ''' Assert list of users is available to everyone '''
        response = self.guest_client.get(self.public_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_user_signup(self):
        ''' Assert new user created successfully '''
        response = self.guest_client.post(
            self.public_url, {'username': 'new_user', 'password': 'password'},
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_obtain_token(self):
        ''' Assert token is issued for a registered user '''
        url = '/api-token-auth/'
        response = self.authorized_client.post(
            url, {'username': 'John', 'password': 'Doe'}, format='json')
        self.assertTrue('token' in response.data, 'No token was found')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_token_for_invalid_credentials(self):
        ''' Assert token is not provided with wrong credentials '''
        url = '/api-token-auth/'
        response = self.authorized_client.post(
            url, {'username': 'Bad', 'password': 'Guy'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_detail_with_token(self):
        ''' Assert details retrieved using token auth '''
        response = self.authorized_client.get(self.private_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_not_allowed_to_edit_other_profiles(self):
        ''' Assert users can't edit information of other users '''
        url = '/api/v1/users/2/'
        response = self.authorized_client.patch(
            url, {'username': 'Bobby'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
