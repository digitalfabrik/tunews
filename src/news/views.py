"""
Simple REST API
"""
import json
import requests

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from basicauth.decorators import basic_auth_required

from .models import NewsLanguage, NewsCategory, NewsItem
from .tunews_clean import clean_html, get_enewsno

def index(request, language_code):  # pylint: disable=W0613
    """
    Display News items
    """
    # pylint: disable=E1101
    filter = ""
    if 'filter' in request.GET:
        filter = str(request.GET['filter'])

    posts = __getFilteredPosts(filter, language_code)
    result = []

    if 'page' in request.GET and 'count' in request.GET:
        page = int(request.GET['page'])
        count = int(request.GET['count'])
        start = count * (page - 1)
        end = (count * page)
        posts = posts[start:end]

    for item in posts:
        result.append(__mapItemToResult(item))

    result_json = json.dumps(result)
    return HttpResponse(result_json, content_type="application/json")


def singlenews(request, news_id):
    item = get_object_or_404(NewsItem, id=news_id)
    result = __mapItemToResult(item)
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


def __getFilteredPosts(filter, language_code):
    if filter == "":
        posts = (NewsItem.objects.filter(pub_date__isnull=False, language__code__contains=language_code).
             order_by('-pub_date'))
    else:
         posts = (NewsItem.objects.filter(
            Q(pub_date__isnull=False) & Q(language__code__contains=language_code) & 
            Q(title__contains=filter) | Q(content__contains=filter)).order_by('-pub_date'))
    
    return posts

def __mapItemToResult(item):
    return {
        'id': item.id,
        'title': item.title,
        'tags': [item.name for item in item.newscategory.all()],
        'date': str(item.pub_date),
        'content': item.content,
        'enewsno': item.enewsno,
    }

@basic_auth_required(
    target_test=lambda request: not request.user.is_authenticated
)
def import_news(request):
    languages = NewsLanguage.objects.filter(wpcategory__isnull=False)
    for language in languages:
        posts = requests.get('https://tunewsinternational.com/wp-json/wp/v2/posts?categories={}'.format(language.wpcategory)).json()
        for post in posts:
            if NewsItem.objects.filter(wppostid=post["id"]):
                continue
            newsitem = NewsItem(
                title=post["title"]["rendered"],
                content=clean_html(post["content"]["rendered"]),
                enewsno=get_enewsno(post["content"]["rendered"]),
                pub_date=post["date"]+"+00:00",
                language=language,
                wppostid=post["id"]
            )
            newsitem.save()
    return HttpResponse([], content_type="application/json")
