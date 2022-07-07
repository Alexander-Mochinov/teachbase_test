import curses
from distutils.command.build_scripts import first_line_re
from django.core.management.base import BaseCommand

from client.models import User, Course
from client.services.client_controller import ClientController

class Command(BaseCommand):
    help = 'Добавление курса'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            user = User.objects.get(id = int(options['user_id'][0]))
            controller = ClientController(user)

            endpoint = f"https://go.teachbase.ru/endpoint/v1/courses"
            courses = controller.send_request(
                path=endpoint,
                method_type="GET",
            ).json()

            for course in courses:
                Course.objects.get_or_create(
                    id = course.get("id", None),
                    name = course.get("name", None),
                    created_at = course.get("created_at", None),
                    updated_at = course.get("updated_at", None),
                    content_type = course.get("content_type", None),
                    owner_name = course.get("owner_name", None),
                    thumb_url = course.get("thumb_url", None),
                    cover_url = course.get("cover_url", None),
                    description = course.get("description", None),
                    last_activity = course.get("last_activity", None),
                    total_score = course.get("total_score", None),
                    total_tasks = course.get("total_tasks", None),
                    is_netology = course.get("is_netology", None),
                    bg_url = course.get("bg_url", None),
                    video_url = course.get("video_url", None),
                    demo = course.get("demo", None),
                    unchangeable = course.get("unchangeable", None),
                    include_weekly_report = course.get("include_weekly_report", None),
                    custom_author_names = course.get("custom_author_names", None),
                    custom_contents_link = course.get("custom_contents_link", None),
                    hide_viewer_navigation = course.get("hide_viewer_navigation", None),
                    duration = course.get("duration", None),
                )
            self.stdout.write(self.style.SUCCESS('Курсы добавленны'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Что то пошло не так :('))