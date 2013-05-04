from wp.models import Post, Category
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content', {'fields':
                     ['post_title',
                      'post_content',
                      'post_category',
                      'post_date',
                      'post_views',
                      'post_status']}),
    ]

    list_display = ('post_title', 'post_status', 'post_date')
    list_filter = ['post_status']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
