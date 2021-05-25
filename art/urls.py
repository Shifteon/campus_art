from django.urls import path
from . import views

urlpatterns = [
    path("", views.art_index, name="art_index"),
    path("category/<category>/", views.art_category, name="art_category"),
    path("building/<building>/", views.art_building, name="art_building"),
]
