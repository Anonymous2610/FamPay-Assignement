from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.YoutubeVideos)
class VideoAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.YoutubeVideos._meta.fields]
	search_fields = ('publish_time', 'video_id',
		'title', 'id')
	list_filter = ('publish_time',)

@admin.register(models.APIKeys)
class APIKeysAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.APIKeys._meta.fields]