from django.contrib import admin
from .models import Article

class ArticleClass(admin.ModelAdmin):
    list_display = (('title'),('slug'),('publish'),('status'),)
    prepopulated_fields = {'slug':('title', )}
    list_filter = ('status', 'publish', )
    ordering = ['publish', ]
    search_fields = ('title', 'description', )

admin.site.register(Article, ArticleClass)

