
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('user_registration', views.UserRegistration.as_view(), name='user_registration'),
    path('login', views.Login.as_view(), name='login'),
    # path('login', views.LoginGenerics.as_view(), name='login'),
    # path('user_registration', views.UserRegistrationGenerics.as_view(), name='user_registration'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)