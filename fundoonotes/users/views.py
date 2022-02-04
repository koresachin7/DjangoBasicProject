"""
* @Author: Sachin S Kore
* @Date: 2022-1-17
* @Title : Fundoo Notes User serializer
"""
import json

from rest_framework.exceptions import ValidationError

from loghandler import logger
from django.contrib.auth.models import auth
# third party imports

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .task import send_mail
from .utility import UserViwe



class UserRegistration(APIView):

    def post(self, request):
        """
            Description:
                This method is writing Registration of user to inserting data
            Parameter:
                using json
            :return : Response
        """
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.create(validate_data=serializer.data)
                send_mail.delay(serializer.data.get("email"))
                return Response({"message": "User Creating Successfully ", "data": serializer.data["username"]},
                                status=status.HTTP_201_CREATED)
        except ValidationError as e:
            logger.error(e)
            return Response({"message": "validation error"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        """
                Description:
                        This method is writing Login of user
                Parameter:
                        using Dictionary
            """
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                token = UserViwe.encode(user.id)
                print(user.id)
                # id = UserViwe().decode(token)
                # print({'id':id['id']})
                return Response({"message": "login successfully", 'jwt':token},status=status.HTTP_200_OK)
            else:
                return Response({"message": "User is invalid", "data": data}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            logger.error(e)
            return Response({"message": "validation error"}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            logger.error(e)
            return Response({"message": "User is invalid"}, status=status.HTTP_403_FORBIDDEN)