import json

import pytest
from rest_framework.reverse import reverse
from notes_app.models import Notes
from notes_app.utility import JWTToke

pytestmark = pytest.mark.django_db
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from users.models import User


@pytest.mark.django_db
def test_notes_post(client, user_data,create_test_user):
    """
        Description:
                This test case method is writing for  Registration of user to inserting data

    """
    data = {
        "username": "gh14",
        "password": "kore14",
    }
    url = reverse("login")
    response = client.post(url, data)
    print(response.content)
    token = response.data["token"]
    print(token)
    headers = {
        'HTTP_AUTHORIZATION':token
    }
    data = {
           "title": "kapil",
           "description": "kp"
    }
    url = reverse("notes_crud")
    response = client.post(url, data,**headers)
    print(response.content)
    assert response.status_code == 201

@pytest.mark.django_db
def test_notes_get(client, user_data, create_test_user):
    """
        Description:
                This test case method is writing for  Registration of user to inserting data

    """
    data = {
        "username": "gh14",
        "password": "kore14",
    }
    url = reverse("login")
    response = client.post(url, data)
    print(response.content)
    token = response.data["token"]
    print(token)
    headers = {
        'HTTP_AUTHORIZATION': token
    }
    data = {
        "title": "kapil",
        "description": "kp"
    }
    url = reverse("notes_crud")
    response = client.post(url, data, **headers)
    assert response.status_code == 201
    url = reverse("notes_crud")
    response = client.get(url,**headers)
    print(response.content)
    assert response.status_code == 201

@pytest.mark.django_db
def test_notes_put(client, user_data, create_test_user):
    """
        Description:
                This test case method is writing for  Registration of user to inserting data

    """
    data = {
        "username": "gh14",
        "password": "kore14",
    }
    url = reverse("login")
    response = client.post(url, data)
    print(response.content)
    token = response.data["token"]
    print(token)
    headers = {
        'HTTP_AUTHORIZATION': token
    }
    data = {
        "title": "kapil",
        "description": "kp",
    }
    url = reverse("notes_crud")
    response = client.post(url, data, **headers)
    print(response.content)
    assert response.status_code == 201
    data = {
        "title": "kp",
        "description": "eng",
        "id": 1
    }
    url = reverse("notes_crud")
    response = client.put(url, data, **headers , content_type='application/json')
    print(response.content)
    assert response.status_code == 201

@pytest.mark.django_db
def test_notes_delete(client, user_data, create_test_user):
    """
        Description:
                This test case method is writing for  Registration of user to inserting data

    """
    data = {
        "username": "gh14",
        "password": "kore14",
    }
    url = reverse("login")
    response = client.post(url, data)
    print(response.content)
    token = response.data["token"]
    print(token)
    headers = {
        'HTTP_AUTHORIZATION': token
    }
    data = {
        "title": "kapil",
        "description": "kp",
    }
    url = reverse("notes_crud")
    response = client.post(url, data, **headers)
    print(response.content)
    assert response.status_code == 201
    data = {
        "id": 1
    }
    url = reverse("notes_crud")
    response = client.delete(url, data, **headers,content_type='application/json')
    print(response.content)
    assert response.status_code == 200

        # from rest_framework.authtoken.models import Token
        #
        # from django.contrib.auth import get_user_model
        #
        # User = get_user_model()
        #
        # self.our_user = User.objects.create(username="testuser", password="abcde")
        #
        # self.token = Token.objects.create(user=self.our_user)
        #
        # print(self.token.key, "token")
        #
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        #

        # self.client = APIClient()
        # print(self.client, "self.client")
        # User = get_user_model()
        # self.our_user = User.objects.create_user("sk70", first_name="mahesh", last_name="kore",
        #                                                password="mahesh123", email="mahesh18@gamil.com", age=26, mobile=9890660608)
        # self.token_url = "http://localhost:8000/api-token-auth/"
        # user_data = {"username": "sk70", "password": "mahesh123"}
        # response = self.client.post(self.token_url, data=user_data)
        # # print(dir(response.), "reponse")
        # print((response.data), "reponse")
        # """
        #         {
        #     "token": "b89d0bab1b4f818c5af6682cec66f84b0bdb664c"
        # }
        # """
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])
        # headers = {
        #     'Authorization': 'Bearer {}'.format()
        # }
        # url = reverse("notes_api_view")
        # user = {"title": "kapil","description": "kp"}
        # response = client.post(url, user,headers=headers)
        # print(response)
        # assert response.status_code == 201
