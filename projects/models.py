from django.db import models


class Project(models.Model):
    project_desc = models.TextField()
    project_title = models.CharField(max_length=300)
    project_stack = models.CharField(max_length=500)
    project_source = models.CharField(max_length=300)
    project_authors = models.CharField(max_length=500)
    project_license = models.CharField(max_length=100)
    thumbnail_link = models.CharField(max_length=300, blank=True)
    screenshot_link = models.CharField(max_length=300, blank=True)
    thumbnail_link2 = models.CharField(max_length=300, blank=True)
    screenshot_link2 = models.CharField(max_length=300, blank=True)
    thumbnail_link3 = models.CharField(max_length=300, blank=True)
    screenshot_link3 = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return self.project_title
