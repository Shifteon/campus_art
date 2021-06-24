from django.urls import path
from .views import ArtworkListView, ArtBuildingCategoryView, BuildingListView 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.map, name="art_map"),
    path("<building>/<category>/<floor>/", ArtBuildingCategoryView.as_view(), name="art_building_category"),
    path("<building>/<category>/", ArtBuildingCategoryView.as_view(), name="art_building_category"), 
]

# be able to import the media
urlpatterns += staticfiles_urlpatterns()