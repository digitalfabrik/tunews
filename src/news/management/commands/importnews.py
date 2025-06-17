import json
import requests

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError

from ...models import NewsLanguage, NewsCategory, NewsItem
from ...tunews_clean import clean_html, get_enewsno


class Command(BaseCommand):
    help = "Get news from tuenews.de"

    def handle(self, *args, **options):
        languages = NewsLanguage.objects.filter(wpcategory__isnull=False)
        for language in languages:
            posts = requests.get('http://tuenews.de/wp-json/wp/v2/posts/?lang={}'.format(language.code)).json()
            print(f"Got {len(posts)} posts.")
            for post in posts:
                if not post["acf"]["integreat"]:
                    continue

                if NewsItem.objects.filter(wppostid=post["id"]):
                    print(f"News {post['id']} already exists.")
                    continue

                newsitem = NewsItem(
                    title=post["title"]["rendered"],
                    content=clean_html(post["content"]["rendered"]),
                    enewsno=post["acf"]["tun_nummer"],
                    pub_date=post["date"]+"+00:00",
                    language=language,
                    wppostid=post["id"]
                )
                newsitem.save()
                print(f"Saving {newsitem}")
