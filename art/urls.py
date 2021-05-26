from django.urls import path
from .views import ArtworkListView, ArtCategoryView
from . import views

urlpatterns = [
    path("", ArtworkListView.as_view(), name="art_index"),
    path("category/<category>", ArtCategoryView.as_view(), name="art_category"),
    path("building/<building>", views.art_building, name="art_building"),
]