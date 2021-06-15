from django.urls import path
from .views import ArtworkListView, ArtCategoryView, ArtBuildingView, ArtBuildingCategoryView, BuildingListView
from . import views

urlpatterns = [
    path("", ArtworkListView.as_view(), name="art_index"),
    path("category/<category>", ArtCategoryView.as_view(), name="art_category"),
    path("building/<building>", ArtBuildingView.as_view(), name="art_building"),
    path("buildings/", BuildingListView.as_view(), name="buildings"),
    path("<building>/<category>/", ArtBuildingCategoryView.as_view(), name="art_building_category"),
    path("map/", views.map, name="art_map"),
]