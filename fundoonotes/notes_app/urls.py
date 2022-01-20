from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# from .views import UserRegistration, Login,LoginSerializer,UserDetail

urlpatterns = [
    path('notes_api_view', views.NotesAPIView.as_view(), name='notes_crud')
]
urlpatterns = format_suffix_patterns(urlpatterns)