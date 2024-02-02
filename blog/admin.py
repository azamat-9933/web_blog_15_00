from django.contrib import admin

from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'created_at')


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
