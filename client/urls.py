from django.urls import path, include

from . import views

urlpatterns = [
    path("", view=views.endpoints, name="endpoints"),
    path("courses/", view=views.get_courses, name="get_courses"),
    path("get_courses_id/<id>/", view=views.get_courses_id, name="get_courses_id"),
    path("users_create/", view=views.users_create, name="users_create"),
    path("course_sessions_register/", view=views.course_sessions_register, name="course_sessions_register"),
    path("get_courses_sessions/", view=views.get_courses_sessions, name="get_courses_sessions"),
    
    # REST URL
    path('api/v1/', include(('client.api.urls'))),
]