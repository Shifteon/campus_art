from django.urls import path
from .views import ArtworkListView, ArtBuildingCategoryView, BuildingListView #, ArtCategoryView, ArtBuildingView, 
from . import views

urlpatterns = [
    path("", ArtworkListView.as_view(), name="art_index"),
    # TODO: Delete these two paths when we are ready to remove the /building/... and /category/... features.
    # path("category/<category>", ArtCategoryView.as_view(), name="art_category"),
    # path("building/<building>", ArtBuildingView.as_view(), name="art_building"),
    path("buildings/", BuildingListView.as_view(), name="buildings"),
    path("<building>/<category>/", ArtBuildingCategoryView.as_view(), name="art_building_category"),
    path("map/", views.map, name="art_map"),
]