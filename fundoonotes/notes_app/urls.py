from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('notes_api_view', views.NotesAPIView.as_view(), name='notes_crud'),
    # path('notes_api_view', views.NotesListGenericsAPIView.as_view(), name='notes_crud'),
    # path('notes_api_detail/<int:id>', views.NotesDetailGenericsAPIView.as_view(), name='notes_crud'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)
