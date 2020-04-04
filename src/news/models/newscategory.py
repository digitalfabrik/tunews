"""
Models
"""
from django.db import models


# pylint: disable=R0903
class NewsCategory(models.Model):
    """
    News categories
    """
    name = models.CharField("Kategorie", max_length=200)

    def __str__(self):
        return self.newscategory

    # pylint: disable=C0111
    class Meta:
        verbose_name = 'Nachrichtenkategorie'
        verbose_name_plural = 'Nachrichtenkategorien'
