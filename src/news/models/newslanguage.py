"""
Models
"""
from django.db import models


# pylint: disable=R0903
class NewsLanguage(models.Model):
    """
    Languages used in news
    """
    language = models.CharField("Sprache", max_length=200)
    code = models.CharField("Sprachcode", max_length=5)
    wpcategory = models.IntegerField("WordPress-Kategorie-ID", null=True, unique=True)

    def __str__(self):
        return self.language

    # pylint: disable=C0111
    class Meta:
        verbose_name = 'Sprache'
        verbose_name_plural = 'Sprachen'
