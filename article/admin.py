from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'slug', 'content')
    # fields = ('id', 'title', 'content ')
    readonly_fields = ('post_time', 'slug')
    search_fields = ('title',)
    ordering = ('id',)
    list_display_links = ("id", "title", "content")


admin.site.register(Article, ArticleAdmin)

