import pytest
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUser:
    def test_user_registration(self, client):
        """
            Description:
                    This test case method is writing for  Registration of user to inserting data
        """
        url = reverse("user_registration")

        user = {"username":"sk101", "first_name":"sachin", "last_name":"kore",
                               "password":"kore123", "email":"sachin@gmail.com", "age":25, "mobile":1111111111}
        response = client.post(url, user)
        assert response.status_code == 201

