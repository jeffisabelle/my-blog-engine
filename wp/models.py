# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    category_title = models.TextField(max_length=100)
    category_slug = models.TextField(max_length=100)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.category_title

    class Meta:
        db_table = u'wp_category'


class Post(models.Model):
    # relations

    # id = models.BigIntegerField(db_column='ID', unique=True)
    # Field name made lowercase.

    post_author = models.BigIntegerField(blank=True)
    post_date = models.DateTimeField(blank=True)
    post_date_gmt = models.DateTimeField(blank=True)
    post_content = models.TextField()
    post_title = models.TextField(max_length=200)
    # post_excerpt = models.TextField(blank=True)
    post_status = models.CharField(max_length=60, blank=True)
    # comment_status = models.CharField(max_length=60, blank=True)
    # ping_status = models.CharField(max_length=60, blank=True)
    # post_password = models.CharField(max_length=60, blank=True)
    post_name = models.CharField(max_length=200)
    # to_ping = models.TextField(blank=True)
    # pinged = models.TextField(blank=True)
    post_modified = models.DateTimeField(blank=True)
    post_modified_gmt = models.DateTimeField(blank=True)
    # post_content_filtered = models.TextField(blank=True)
    post_parent = models.BigIntegerField(blank=True)
    # guid = models.CharField(max_length=765, blank=True)
    # menu_order = models.IntegerField(blank=True)
    post_type = models.CharField(max_length=60, blank=True)
    # post_mime_type = models.CharField(max_length=300, blank=True)
    # comment_count = models.BigIntegerField(blank=True)

    post_category = models.ManyToManyField(Category)
    post_views = models.IntegerField()

    def save(self, *args, **kwargs):
        current_time = datetime.now()

        p = Post.objects.filter(post_name=slugify(self.post_title))
        print "\n\n"
        print p
        print "\n\n"

        if not p:
            self.post_author = 1
            self.post_date = current_time
            self.post_date_gmt = current_time
            self.post_name = slugify(self.post_title)
            self.post_status = "publish"
            self.post_type = "post"
            self.post_parent = 0
            self.menu_order = 0
            self.comment_count = 0
            self.post_views = 0

        self.post_modified = current_time
        self.post_modified_gmt = current_time

        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.post_title

    class Meta:
        db_table = u'wp_posts'
