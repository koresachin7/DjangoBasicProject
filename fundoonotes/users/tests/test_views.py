import json

import pytest
from rest_framework.reverse import reverse
from users.models import User
from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db


class TestUser:
    @pytest.mark.django_db
    def test_user_registration(self, client):
        """
            Description:
                    This test case method is writing for  Registration of user to inserting data
        """
        url = reverse("user_registration")

        user = {"username": "sk101", "first_name": "sachin", "last_name": "kore",
                "password": "kore123", "email": "sachin@gmail.com", "age": 25, "mobile": 1111111111}

        response = client.post(url, user)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_login_validation(self, client):
        """
            Description:
                        This test case method is writing for  Login of user to inserting data and check user login
        """
        user = {"username": "sk101", "first_name": "sachin", "last_name": "kore",
                "password": "kore123", "email": "sachin@gmail.com", "age": 25, "mobile": 1111111111}
        users = User.objects.create_user(**user)
        users.is_verified = True
        users.save()
        data = {
            "username": "sk101",
            "password": "kore123",
        }
        headers = {
            'content_type': 'application/json'
        }
        url = reverse("login")
        response = client.post(url, data, **headers)
        print(response.content)
        assert response.status_code == 200
