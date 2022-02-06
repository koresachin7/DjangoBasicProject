from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
# from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
#
# schema_view = get_swagger_view(title='Pastebin API')

from . import views

# from .views import UserRegistration, Login,LoginSerializer,UserDetail

urlpatterns = [
    path('notes_api_view', views.NotesAPIView.as_view(), name='notes_crud'),
]
urlpatterns = format_suffix_patterns(urlpatterns)