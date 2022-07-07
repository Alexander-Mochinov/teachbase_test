from django.urls import path

from client.api.rest_views import (
    courses_list,
    detail_courses,
)

urlpatterns = [
    path("course/<id>/", view=detail_courses, name="detail_courses"),
    path("courses-list/", view=courses_list, name="courses_list"),
]