from django.contrib import admin
from .models import NewsCategory, NewsLanguage, NewsItem


admin.site.register(NewsCategory)
admin.site.register(NewsLanguage)
admin.site.register(NewsItem)
