"""
* @Author: Sachin S Kore
* @Date: 2022-1-11
* @Title : Fundoo Notes User authenticate
"""
import json

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import auth
from .models import User


@csrf_exempt
def user_registration(request):
    """
    Description:
        This method is writing Registration of user
    Parameter:
        using Dictionary
    """

    try:

        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")

            if User.objects.filter(username=username).exists():
                return JsonResponse({"message":"Username is already Take","data":{"username": username}})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({"message":"email is already Take","data":{"email": email}})
            else:
                user = User.objects.create_user(username=username, first_name=data.get("first_name"), last_name=data.get("last_name"),
                                                password=data.get("password"), email=email,age=data.get("age"), mobile=data.get("mobile"))
                user.save()
                return JsonResponse({"message":"User data Successfully Sava","data": data})
    except Exception as e:
        return HttpResponse("Data is invalid",e)


def login(request):
    """
        Description:
            This method is writing Login of user
        Parameter:
            using Dictionary
    """
    if request.method == "POST":
        data = json.loads(request.body)
        user = auth.authenticate(username=data.get("username"), password=data.get("password"))

        if user is not None:
            return JsonResponse({"message":"login successfully","data": data})
        else:
            return JsonResponse({"message":"User is invalid","data": data})
