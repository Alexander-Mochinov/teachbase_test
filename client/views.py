from pydoc import cli
from django.http import JsonResponse
from django.shortcuts import render

from client.services.client_controller import ClientController


def endpoints(request):
    context = {}
    client = ClientController(request.user)
    context["endpoints"] = client.api_url()
    return render(request, "components/endpoints.html", context)

def get_courses(request):
    """список курсов"""

    context = {}
    client = ClientController(request.user)
    endpoint = f"https://go.teachbase.ru/endpoint/v1/courses"
    context["request"] = client.send_request(
        path=endpoint,
        method_type="GET",
    ).json()
    return JsonResponse(context)

def get_courses_id(request, id):
    """детальное представление курса"""
    
    context = {}
    client = ClientController(request.user)
    endpoint = f"https://go.teachbase.ru/endpoint/v1/courses/{id}"
    context["request"] = client.send_request(
        path=endpoint,
        method_type="GET",
    ).json()
    return JsonResponse(context)

def users_create(request):
    """создание пользователя"""
    
    context = {}
    client = ClientController(request.user)
    
    endpoint = f"https://go.teachbase.ru/endpoint/v1/users/create"
    params = {
        "users": [
            {
                "email": "test@teachbase.ru",
                "name": "John",
                "description": "Corrupti natus quia recusandae.",
                "last_name": "Doe",
                "phone": "",
                "role_id": 1,
                "auth_type": 0,
                "external_id": "u-007",
                "password": "qwerty",
                "lang": "ru"
            }
        ],
        "options": {
            "activate": True,
            "verify_emails": True,
            "skip_notify_new_users": True,
            "skip_notify_active_users": True,
        },
        "external_labels": True,
    }
    context["request"] = client.send_request(
        path=endpoint,
        json=params,
        method_type="POST",
    ).json()

    return JsonResponse(context)

def course_sessions_register(request):
    """запись пользователя на сессию"""
    
    context = {}
    client = ClientController(request.user)
    endpoint = f"https://go.teachbase.ru/endpoint/v1/course_sessions/154587/register"
    params = {
        "email": "email_1_2@factory.tb",
        "phone": 792177788666,
        "user_id": 334
    }
    context["request"] = client.send_request(
        path=endpoint,
        json=params,
        method_type="POST",
    ).json()

    return JsonResponse(context)

def get_courses_sessions(request):
    """сессии курсов"""
    
    context = {}
    client = ClientController(request.user)
    endpoint = f"https://go.teachbase.ru/endpoint/v1/courses/154587/course_sessions?filter=active"
    context["request"] = client.send_request(
        path=endpoint,
        method_type="GET",
    ).json()

    return JsonResponse(context)