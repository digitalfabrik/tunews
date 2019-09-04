"""
Simple REST API
"""
from django.http import HttpResponse
from django.core import serializers

from .models import NewsLanguage, NewsCategory, NewsItem


def index(request):  # pylint: disable=W0613
    """
    Display News items
    """
    # pylint: disable=E1101
    posts = (NewsItem.objects.filter(pub_date__isnull=False).
             order_by('-pub_date'))
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="application/json")


def categories(request):  # pylint: disable=W0613
    """
    List categories
    """
    # pylint: disable=E1101
    news_categories = NewsCategory.objects.all()
    categories_list = serializers.serialize('json', news_categories)
    return HttpResponse(categories_list, content_type="application/json")


def languages(request):  # pylint: disable=W0613
    """
    List languages
    """
    # pylint: disable=E1101
    news_languages = NewsLanguage.objects.all()
    languages_list = serializers.serialize('json', news_languages)
    return HttpResponse(languages_list, content_type="application/json")
