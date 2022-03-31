from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thambnail(self, object):
        return format_html('<img src="{}" width="40" style= "border-radius : 50px" />'.format(object.photo.url))
    
    thambnail.short_description ="photo" 

    list_display = ("id", "thambnail", "first_name", "designation", "created_date", )
    list_display_links = ("id", "thambnail", "first_name", )
    search_fields = ("first_name", "last_name",  "designation",)
    list_filter = ("designation", )

admin.site.register(models.Team,TeamAdmin)