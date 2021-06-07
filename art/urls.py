from django.urls import path
from .views import ArtworkListView, ArtCategoryView, ArtBuildingView
from . import views

urlpatterns = [
    path("", ArtworkListView.as_view(), name="art_index"),
    path("category/<category>", ArtCategoryView.as_view(), name="art_category"),
    path("building/<building>", ArtBuildingView.as_view(), name="art_building"),

    # For the map
    #path("map/"), CampusMapView.as_view(), name="art_map"),
    path("map/", views.map, name="art_map"),

]