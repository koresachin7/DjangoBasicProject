"""
* @Author: Sachin S Kore
* @Date: 2022-1-19
* @Title : CRUD operation in class function
"""

from loghandler import logger
# third party imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NotesSerializer
from .models import Notes


class NotesAPIView(APIView):
    """
    Description: This Class using for Note app Operation
    """

    def post(self, request):
        """
            Description:
                This method is writing Registration of user to inserting data
            Parameter:
                using json
            :return : Response
        """
        try:
            serializer = NotesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Note Creating Successfully ", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        this method is created for retrieve data
        :param request: format of the request
        :return: Response
        """
        try:
            notes = Notes.objects.filter(user_id=request.GET.get("user_id"))
            serializer = NotesSerializer(notes, many=True)
            return Response({"message": "get Note  Successfully ", "data": serializer.data},
                            status=status.HTTP_201_CREATEDserializer.data)
        except Exception as e:
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        """
        this method is update for using retrieve data
        :param request: format of the request
        :return: Response
        """

        try:
            notes = Notes.objects.get(id=request.data.get("id"))
            serializer = NotesSerializer(instance=notes, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Note Update Successfully ", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        this method is delete for using  retrieve data
        :param request: format of the request
        :return: Response
        """

        try:
            notes = Notes.objects.get(id=request.data.get("id"))
            notes.delete()
            return Response({"message": "Item successfully delete", },
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)
