from django.core.management.base import BaseCommand
from helpdesk.models import HelpVideo

class Command(BaseCommand):
    help = 'Seed initial help videos'

    def handle(self, *args, **kwargs):
        videos = [
            {"app_name": "Workato", "video_title": "Workato Basics", "video_url": "https://youtu.be/workato1"},
            {"app_name": "Workato", "video_title": "Workato Advanced", "video_url": "https://youtu.be/workato2"},
            {"app_name": "Alteryx", "video_title": "Alteryx Getting Started", "video_url": "https://youtu.be/alteryx1"},
            {"app_name": "AWS", "video_title": "AWS Cloud Overview", "video_url": "https://youtu.be/aws1"},
        ]
        for v in videos:
            HelpVideo.objects.get_or_create(**v)
        self.stdout.write(self.style.SUCCESS('Seeded help videos.'))
