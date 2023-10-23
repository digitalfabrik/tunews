from django.urls import path

from . import views

urlpatterns = [
    path('tags', views.categories),
    path('languages', views.languages),
    path('<int:news_id>', views.singlenews, name='singlenews'),
    path('<str:language_code>', views.index, name='index'),
]
