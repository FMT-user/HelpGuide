from django.contrib import admin
from .models import HelpVideo

@admin.register(HelpVideo)
class HelpVideoAdmin(admin.ModelAdmin):
    list_display = ("app_name", "video_title", "video_url")
    search_fields = ("app_name", "video_title")
