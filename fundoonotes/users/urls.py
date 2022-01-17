from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# from .views import UserRegistration, Login,LoginSerializer,UserDetail
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('UserRegistration', views.UserRegistration.as_view(), name='test'),
    path('Login', views.Login.as_view(), name='Login'),
    # path('LoginSerializer', views.LoginSerializer.as_view(), name='LoginSerializer'),
    # path('UserDetail/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)