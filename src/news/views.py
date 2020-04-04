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

    posts = (NewsItem.objects.filter(pub_date__isnull=False, language__code__contains=language_code).
             order_by('-pub_date'))
    result = []
    if 'page' in request.GET and 'count' in request.GET:
        page = int(request.GET['page'])
        count = int(request.GET['count'])
        start = count * (page - 1)
        end = (count * page)
        posts = posts[start:end]
    for item in posts:
        result.append({'id': item.id, 'title': item.title, 'tags': [item.name for item in item.newscategory.all()], 'date': str(item.pub_date)})
    result_json = json.dumps(result)
    return HttpResponse(result_json, content_type="application/json")

def singlenews(request, news_id):
    item = NewsItem.objects.filter(id=news_id)[0]
    result = {
        'id': item.id,
        'title': item.title,
        'tags': [item.name for item in item.newscategory.all()],
        'date': str(item.pub_date),
        'content': item.content,
        'enewsno': item.enewsno,
    }
    return HttpResponse(json.dumps(result), content_type="application/json")

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
    result = []
    for language in news_languages:
        result.append({'code': language.code, 'name': language.language})
    return HttpResponse(json.dumps(result), content_type="application/json")
