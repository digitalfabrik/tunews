"""
Simple REST API
"""
from django.http import HttpResponse
from django.core import serializers
import json
from .models import NewsLanguage, NewsCategory, NewsItem


def index(request, language_code):  # pylint: disable=W0613
    """
    Display News items
    """
    # pylint: disable=E1101
    print(language_code)
    posts = (NewsItem.objects.filter(pub_date__isnull=False, language__code__contains=language_code).
             order_by('-pub_date'))
    result = []
    for item in posts:
        result.append({'id': item.id, 'title': item.title, 'tags': [item.name for item in item.newscategory.all()], 'date': str(item.pub_date)})
    result_json = json.dumps(result)
    return HttpResponse(result_json, content_type="application/json")

def singlenews(request, news_id):
    print(news_id)
    result = ""
    return HttpResponse(result)

def categories(request):  # pylint: disable=W0613
    """
    List categories
    """
    # pylint: disable=E1101
    news_categories = NewsCategory.objects.all()
    result = []
    for category in news_categories:
        result.append({'id': category.id, 'name': category.name})
    return HttpResponse(json.dumps(result), content_type="application/json")


def languages(request):  # pylint: disable=W0613
    """
    List languages
    """
    # pylint: disable=E1101
    news_languages = NewsLanguage.objects.all()
    languages_list = serializers.serialize('json', news_languages)
    return HttpResponse(languages_list, content_type="application/json")
