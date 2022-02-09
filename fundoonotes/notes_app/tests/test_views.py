import pytest
from rest_framework.reverse import reverse
from notes_app.models import Notes

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUser:
    pass