"""
Simple REST API
"""

import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import NewsLanguage, NewsCategory, NewsItem


def index(request, language_code):
    """
    Display News items
    """
    filter = ""
    if "filter" in request.GET:
        filter = str(request.GET["filter"])

    posts = __getFilteredPosts(filter, language_code)
    result = []

    if "page" in request.GET and "count" in request.GET:
        page = int(request.GET["page"])
        count = int(request.GET["count"])
        start = count * (page - 1)
        end = count * page
        posts = posts[start:end]

    for item in posts:
        result.append(__mapItemToResult(item))

    result_json = json.dumps(result)
    return HttpResponse(result_json, content_type="application/json")


def singlenews(request, news_id):
    item = get_object_or_404(NewsItem, id=news_id)
    result = __mapItemToResult(item)
    return HttpResponse(json.dumps(result), content_type="application/json")


def categories(request):
    """
    List categories
    """
    news_categories = NewsCategory.objects.all()
    result = []
    for category in news_categories:
        result.append({"id": category.id, "name": category.name})
    return HttpResponse(json.dumps(result), content_type="application/json")


def languages(request):
    """
    List languages
    """
    news_languages = NewsLanguage.objects.all()
    result = []
    for language in news_languages:
        result.append({"code": language.code, "name": language.language})
    return HttpResponse(json.dumps(result), content_type="application/json")


def __getFilteredPosts(filter, language_code):
    if filter == "":
        posts = NewsItem.objects.filter(
            pub_date__isnull=False, language__code__contains=language_code
        ).order_by("-pub_date")
    else:
        posts = NewsItem.objects.filter(
            Q(pub_date__isnull=False)
            & Q(language__code__contains=language_code)
            & Q(title__contains=filter)
            | Q(content__contains=filter)
        ).order_by("-pub_date")

    return posts


def __mapItemToResult(item):
    return {
        "id": item.id,
        "title": item.title,
        "tags": [item.name for item in item.newscategory.all()],
        "date": str(
            item.pub_date
        ),  # this field should be deleted in summer of 2026, as we want to use the field `display_date` going forward
        "display_date": str(item.pub_date.isoformat()),
        "content": item.content,
        "enewsno": item.enewsno,
    }
