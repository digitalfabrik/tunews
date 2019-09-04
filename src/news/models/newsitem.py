"""
Models
"""
from django.db import models
from . import NewsCategory, NewsLanguage


# pylint: disable=R0903
class NewsItem(models.Model):
    """
    Actual TuNews
    """
    title = models.CharField("Titel", max_length=200)
    content = models.TextField("Inhalt")
    enewsno = models.CharField("E-News Nummer", max_length=20)
    pub_date = models.DateTimeField('Datum')
    newscategory = models.ManyToManyField(NewsCategory)
    language = models.ForeignKey(NewsLanguage, on_delete=models.CASCADE)

    def __str__(self):
        return self.language.language + ": " + self.title + " - " + self.enewsno

    # pylint: disable=C0111
    class Meta:
        verbose_name = 'Nachricht'
        verbose_name_plural = 'Nachrichten'
