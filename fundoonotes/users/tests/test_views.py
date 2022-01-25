import pytest
from rest_framework.reverse import reverse
from users.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUser:
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

    def test_login_validation(self, client):
        """
            Description:
                        This test case method is writing for  Login of user to inserting data and check user login
        """
        user = User.objects.create_user("sk70", first_name="mahesh", last_name="kore", password="mahesh123", email="mahesh18@gamil.com", age=26, mobile=9890660608)
        user.is_verified = True
        user.save()
        data = {
            "username": "sk70",
            "password": "mahesh123",
        }
        url = reverse("login")
        response = client.post(url, data)
        assert response.status_code == 200
