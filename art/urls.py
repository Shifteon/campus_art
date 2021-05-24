from django.urls import path
from . import views

app = 'art'
urlpatterns = [
    path('building/', views.building, name='building')
]