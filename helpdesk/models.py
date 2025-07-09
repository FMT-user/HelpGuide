from django.db import models

class HelpVideo(models.Model):
    app_name = models.CharField(max_length=100)
    video_title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return f"{self.app_name} - {self.video_title}"
