from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from client.api.serializers import CourseSerializer
from client.models import (
    Course,
)

@api_view(['GET',])
def courses_list(request):
    """
    Список курсов

    List courses
    """

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def detail_courses(request, id):
    """
    Детализация курса

    Course detail
    """

    if request.method == 'GET':
        courses = Course.objects.filter(id = id)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
