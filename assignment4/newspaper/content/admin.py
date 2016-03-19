from django.contrib import admin

from .models import Article, Image, Contributor

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Title/Subtitle Information', {'fields': ['title', 'subtitle']}),
    ('Publication Date', {'fields': ['pub_date']}),
    ('Writer', {'fields': ['contributors']}),
    ('Content', {'fields': ['text', 'post_script']}),
    ]
    list_display = ('title', 'pub_date')

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Title/Subtitle Information', {'fields': ['title', 'subtitle']}),
    ('Publication Date', {'fields': ['pub_date']}),
    ('Photographer/Image Editor', {'fields': ['contributors']}),
    ('Image Location', {'fields': ['path']}),
    ]
    list_display = ('title', 'pub_date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Contributor)

# username: admin
# password: 1234abcd
