from django.urls import path

from . import views

urlpatterns = [
    path('items', views.index, name='index'),
    path('tags', views.categories),
    path('languages', views.languages)
]
