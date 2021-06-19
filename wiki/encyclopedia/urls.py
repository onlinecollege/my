from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lib/<str:title>", views.lib, name="lib"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("guide", views.guide, name="guide")
]
