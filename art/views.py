from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Building_Name, Category, Artwork


class ArtworkListView(ListView):
    model = Artwork
    template_name = 'art_index.html'
    context_object_name = "artwork"     # This is the name of the object that is called in the html file.


class ArtBuildingCategoryView(ListView):
    model = Artwork
    template_name = 'art_building_category.html'
    context_object_name = 'artwork'

    def get_context_data(self, **kwargs):   # Do you think it would be possible to give a 404 message if the user navigates to a building that doesn't exist?
        context = super(ArtBuildingCategoryView, self).get_context_data(**kwargs)
        building_art = Artwork.objects.filter(building__name__contains=self.kwargs['building'])
        context['art_context'] = building_art.filter(categories__name__contains=self.kwargs['category'], floor=self.kwargs['floor'])
        # Try to add an if statement make art_context a different thing in floor == 0.

        context['category_names'] = Category.objects.all().order_by('name')
        context['building_names'] = Building_Name.objects.all().order_by('name')
        return context

# Add another view, use an if statement, change database

class BuildingListView(ListView):
    model = Building_Name
    template_name = 'buildings.html'
    context_object_name = 'buildings'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ArtDetailView(DetailView):
    model = Artwork
    template_name = 'art_detail.html'
    context_object_name = 'artwork'


def map(request):
    return render(request, "map.html")

