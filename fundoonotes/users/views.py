"""
* @Author: Sachin S Kore
* @Date: 2022-1-8
* @Title : Fundoo Notes User Registration
"""
import json

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
            user_name = data.get("user_name")

            if User.objects.filter(user_name=user_name).exists():
                return JsonResponse({"message": "Username is already Take", "data": {"username": user_name}})
            else:
                user = User(user_name=user_name, first_name=data.get("first_name"), last_name=data.get("last_name"),
                            mobile=data.get("mobile"),
                            password=data.get("password"), is_verified=data.get("is_verified"))
                user.save()
                return JsonResponse({"message": "User data Successfully Sava", "data": data})
    except Exception as e:
        return HttpResponse("Data is invalid", e)


def login(request):
    """
        Description:
            This method is writing Login of user
        Parameter:
            using Dictionary
    """
    if request.method == "POST":
        data = json.loads(request.body)
        user_name = data.get("user_name")
        password = data.get("password")

        if User.objects.filter(user_name=user_name, password=password):
            return HttpResponse("User is valid")
        else:
            return HttpResponse("User is invalid")
