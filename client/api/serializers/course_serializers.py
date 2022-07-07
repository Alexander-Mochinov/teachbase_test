import imp
from rest_framework import serializers

from client.models import (
    Course,
)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "name", "created_at", "updated_at", "content_type", "owner_name",
            "thumb_url", "cover_url", "description", "last_activity",
            "total_score", "total_tasks", "is_netology", "bg_url",
            "video_url", "demo", "unchangeable", "include_weekly_report", "custom_author_names",
            "custom_contents_link", "hide_viewer_navigation", "duration", "account", "authors", "types",
        ]
