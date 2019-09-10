from django.contrib import admin
from Article.models import *

admin.site.register(Author)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","public_time","description"]
admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleType)
# Register your models here.
