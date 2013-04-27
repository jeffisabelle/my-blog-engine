from projects.models import Project
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_source')

admin.site.register(Project, ProjectAdmin)
