
"""
* @Author: Sachin S Kore
* @Date: 2022-2-09
* @Title : CRUD operation in class function
"""

from rest_framework import generics
from .serializers import NotesSerializer
from .models import Notes
from rest_framework import permissions
from .permissions import IsOwner


class NotesListGenericsAPIView(generics.ListCreateAPIView):

    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """
           Description:
                    This method use for post data
        """
        return serializer.save(id=self.request.data.get("id"))

    def get_queryset(self):
        """
            Description:
                    This method use for get data
        """
        return self.queryset.filter(user_id=self.request.data.get("user_id"))


class NotesDetailGenericsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
    permissions = (permissions.IsAuthenticated,IsOwner,)
    lookup_field = "id"

    def perform_create(self, serializer):
        """
            Description:
                    This method use for put data
        """
        return serializer.save(data=self.request.data)

    def get_queryset(self):
        """
            Description:
                    This method use for delete data
        """
        return self.queryset.filter(id=self.request.data.get("id"))
