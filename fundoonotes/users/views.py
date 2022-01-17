"""
* @Author: Sachin S Kore
* @Date: 2022-1-17
* @Title : Fundoo Notes User serializer
"""
import json
from loghandler import logger
from django.contrib.auth.models import auth
# third party imports

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer


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
            if serializer.is_valid():
                serializer.create(validate_data=serializer.data)
                return Response({"message": "User Creating Successfully ", "data": serializer.data["username"]})
        except Exception as e:
            logger.error(e)
            return Response({"message": "invalidate credentials"}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    try:
        def post(self, request):
            """
                Description:
                        This method is writing Login of user
                Parameter:
                        using Dictionary
            """
            data = json.loads(request.body)
            user = auth.authenticate(username=data.get("username"), password=data.get("password"))

            if user is not None:
                return Response({"message": "login successfully", "data": data})
            else:
                return Response({"message": "User is invalid", "data": data})

    except Exception as e:
              Response(e)
