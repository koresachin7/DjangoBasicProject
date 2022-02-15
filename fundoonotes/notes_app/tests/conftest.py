import pytest
from users.models import User


@pytest.fixture
def user_data():
    return {"username": "gh14", "first_name": "sachin", "last_name": "kore",
                "password": "kore14", "email": "sachn@gmail.com", "age": 25, "mobile": 1111111111}


@pytest.fixture
def create_test_user(user_data):
    test_user = User.objects.create_user(**user_data)
    test_user.is_verified = True
    return test_user



