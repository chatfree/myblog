from django.contrib import admin

from . import models

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created')
    list_filter=("created",)

admin.site.register(models.Article,ArticleModelAdmin)
