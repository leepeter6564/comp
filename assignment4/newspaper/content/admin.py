from django.contrib import admin

from .models import Article, Image, Contributor

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Contributor)

# username: admin
# password: 1234abcd