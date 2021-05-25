from django.urls import path
from . import views

urlpatterns = [
    path("", views.art_index, name="art_index"),
    path("<category>/", views.art_category, name="art_category"),
    path("<buildingy>/", views.art_building, name="art_building"),
