import time
import json
import requests
from datetime import datetime

from django.conf import settings

from client.models import (
    User,
    AuthorizationData,
)


class ClientController:
    """Класс контроллер"""

    API_HOST_NAME = settings.API_HOST
    AUTHORIZATION_RESOURCE_PATH = "https://go.teachbase.ru/oauth/token/"

    REQUEST_METHODS = {
        "GET": requests.get,
        "POST": requests.post,
        "DELETE": requests.delete,
        "PUT": requests.put,
        "PATCH": requests.patch,
    }

    def __init__(self, user: User, *args, **kwargs) -> None:

        self.user = user
        self.authorizations_user_data = self.authorizations_data()


    def authorizations_data(self) -> dict:
        """
        Метод авторизации
        Отправка запроса по api для авторизации
        Методо заполняет данные модели клиента
        Заполняет модель новыми данными
        Такими как:
            [access_token, token_type, expires_in, created_at, resource_owner_id]

        При новой отправке запроса пертирает новыми данными модель ClientParametrs

        Authorization method
        Sending an api request for authorization
        The method populates the client model data populates the model with new data such as
            [access_token, token_type, expires_in, created_at, resource_owner_id]

        When a new request is sent, it overwrites the EndpointParameters model with new data
        """

        data_user_authorizations = self.get_or_update_token()
        authorization_data = AuthorizationData.objects.filter(user = self.user)

        if authorization_data.exists():
            authorization_data = authorization_data.first()
            if self.check_token(authorization_data.access_token):
                return authorization_data

            else:
                authorization_data.access_token = data_user_authorizations["access_token"]
                authorization_data.token_type = data_user_authorizations["token_type"]
                authorization_data.resource_owner_id = data_user_authorizations["resource_owner_id"]
                # authorization_data.expires_in = self.convert_to_preferred_format(
                #     data_user_authorizations["expires_in"],
                # )
                # authorization_data.created_at = self.utcfromtimestamp(
                #     data_user_authorizations["created_at"],
                #)
                authorization_data.save()
        else:
            authorization_data = AuthorizationData.objects.create(
                access_token = data_user_authorizations["access_token"],
                token_type = data_user_authorizations["token_type"],
                resource_owner_id = data_user_authorizations["resource_owner_id"],
                # expires_in = self.convert_to_preferred_format(
                #     data_user_authorizations["expires_in"],
                # ),
                # created_at = self.utcfromtimestamp(
                #     data_user_authorizations["created_at"],
                # ),
            )

        return authorization_data

    def send_request(
        self,
        path: str,
        method_type: str,
        params: dict = {},
        json: dict = {},
        headers: dict = {},
        data: dict = {},
        authorization: bool = False,
        **kwargs,
    ) -> requests:
        """
        Выполняет отправку запроса c параметрами

        Sends a request with parameters
        """

        if not authorization:
            if self.authorizations_user_data:
                headers["authorization"] = f'Bearer {self.authorizations_user_data.access_token}'
                headers["accept"] = "application/json"

        return self.REQUEST_METHODS[method_type](
            url=path,
            params=params,
            headers=headers,
            data=data,
            json=json,
            **kwargs,
        )


    def check_token(self, token: str) -> requests:
        """
        Проверяет текущий access_token
        Закончился ли лимит использования

        Checks the current access_token
        Has the usage limit expired
        """

        check_endpoint_string = f'{self.API_HOST_NAME}/_ping?access_token={token}'

        return self.send_request(
            path=check_endpoint_string,
            method_type="GET",
            authorization=True, 
        ).ok


    def get_or_update_token(self) -> json:
        """
        Метод получения токена или его обновление

        Method of obtaining a token or its renewal
        """

        data_user_authorizations = self.REQUEST_METHODS["POST"](
            url=self.AUTHORIZATION_RESOURCE_PATH,
            data={
                "client_id": settings.CLIENT_ID_KEY,
                "client_secret": settings.CLIENT_SECRET_API_KEY,
                "grant_type": settings.GRANT_TYPE,
            },
        ).json()

        return data_user_authorizations


    def utcfromtimestamp(self, date_number: int) -> datetime:
        """Перевод числа в дату"""

        return datetime.utcfromtimestamp(
            date_number + 1262304000
        )


    def convert_to_preferred_format(self, seconds: int) -> str:
        """Перевод числа на часы"""
        
        return time.strftime(
            "%H:%M:%S", 
            time.gmtime(seconds)
        )

    def api_url(self):
        """Захардкоженный список endpoints"""

        urls = {
            "courses": {
                "name": "Список курсов",
                "path": "https://go.teachbase.ru/endpoint/v1/courses",
                "inner_path": "courses/",
                "params": {},
                "method_type": "GET",
            },
            "detaile_cource": {
                "name": "Детальный курс под id №154587",
                "path": "https://go.teachbase.ru/endpoint/v1/courses/<id>",
                "inner_path": "get_courses_id/154587/",
                "params": {},
                "method_type": "GET",
            },
            "users_create": {
                "name": "Создание пользователя",
                "path": "https://go.teachbase.ru/endpoint/v1/users/create",
                "inner_path": "users_create/",
                "params": {
                    "users": [
                        {
                        "email": "test@teachbase.ru",
                        "name": "John",
                        "description": "Corrupti natus quia recusandae.",
                        "last_name": "Doe",
                        "phone": "null",
                        "role_id": 1,
                        "auth_type": 0,
                        "external_id": "u-007",
                        "labels": {
                            "1": "2",
                            "3": "4"
                        },
                        "external_labels": {
                            "1": "2",
                            "3": "4"
                        },
                        "password": "qwerty",
                        "lang": "ru"
                        }
                    ],
                    "options": {
                        "activate": True,
                        "verify_emails": True,
                        "skip_notify_new_users": True,
                        "skip_notify_active_users": True
                    },
                    "external_labels": True,
                },
                "method_type": "POST",
            },
            "sessions_register": {
                "name": "запись пользователя на сессию",
                "path": "https://go.teachbase.ru/endpoint/v1/course_sessions/154587/register",
                "inner_path": "course_sessions_register/",
                "params": {
                    "email": "email_1_2@factory.tb",
                    "phone": 792177788666,
                    "user_id": 334,
                },
                "method_type": "POST",
            },
            "sessions_course": {
                "name": "Сессии курса",
                "path": "https://go.teachbase.ru/endpoint/v1/courses/154587/course_sessions?filter=active",
                "inner_path": "get_courses_sessions/",
                "params": {},
                "method_type": "GET",
            }
        }

        return urls