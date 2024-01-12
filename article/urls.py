from django.urls import path
from .views import (
    index,
    article_detail,
    article_create,
    article_change,
    article_create_form,
    article_delete)

urlpatterns = [
    path('', index, name='list'),
    path('detail<slug:slug>', article_detail, name='info'),
    path('create', article_create, name='create'),
    path('change<slug:slug>', article_change, name='change'),
    path("formcreate", article_create_form, name="create_form"),
    path('delete<slug:slug>', article_delete, name="delete"),
]