__author__ = 'mengmeng'
from django.contrib import admin


# class PostAdmin(admin.ModelAdmin):
#     fields = ('published','title','content','author','slug',)
#     list_display = ('title','updated_at','published',)
#     list_display_links = ('title',)
#     list_editable = ('published',)
#     ordering = ('-id',)
#     list_filter = ('published','updated_at','author',)
#     prepopulated_fields = {"slug": ("title",)}
#     # readonly_fields = ('slug',)
#     search_fields = ['title','content']
#
# admin.site.register(Post,PostAdmin)