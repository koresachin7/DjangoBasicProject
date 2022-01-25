"""
* @Author: Sachin S Kore
* @Date: 2022-1-19
* @Title : CRUD operation in class function
"""
import json

from loghandler import logger
# third party imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from notes_app.serializers import NotesSerializer
from notes_app.models import Notes
from notes_app.utility import RedisOperations


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
            RedisOperations().post_to_cache(request.data.get("user_id"), json.dumps(serializer.data))
            return Response({"message": "Note Creating Successfully ", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
           Description:
                       this method is created for retrieve data
           :param request: format of the request
           :return: Response
        """
        try:

            notes = Notes.objects.filter(user_id = request.GET.get("user_id"))
            serializer = NotesSerializer(notes, many=True)
            RedisOperations().get_to_cashe(request.GET.get("user_id"))
            return Response({"message": "get Note Data  Successfully ","data": serializer.data},status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({"message": "invalidate credentials"},status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
           Description:
                      this method is update for using retrieve data
           :param request: format of the request
           :return: Response
        """

        try:
            notes = Notes.objects.get(id=request.data.get("id"))
            serializer = NotesSerializer(instance=notes, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # Redis().redis_put(request.data.get("id"), json.dumps(serializer.data))
            return Response({"message": "Note Update Successfully ", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
           Description:
                     this method is delete for using  retrieve data
           :param request: format of the request
           :return: Response
        """

        try:
            notes = Notes.objects.get(id=request.data.get("id"))
            if notes is not None:
                notes.delete()
                return Response({"message": "Delete successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "ID is invalid"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
               logger.error(e)
               return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)