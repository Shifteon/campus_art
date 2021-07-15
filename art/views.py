from django.shortcuts import render
from django.urls import reverse
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
        building_art = Artwork.objects.filter(building__name__contains=self.kwargs['building']).order_by('floor')

        if self.kwargs['floor'] == '0':   # Load all art in the building if the floor in url is zero.
            context['art_context'] = building_art.filter(categories__name__contains=self.kwargs['category']).order_by('floor', 'title')
            context['categories_for_filter'] = building_art.values('categories').order_by('categories')
            # Specifying .order_by(categories__name) to the context above will order by the 'name' field in the 'categories' model. 
            #  I added a default ordering to the Categories model. We still need to specify to order by categories,
            #  but the categories model will now order by the 'name' field by default (instead of order inserted into database).
        else:
            context['art_context'] = building_art.filter(categories__name__contains=self.kwargs['category'], floor=self.kwargs['floor'])
            context['categories_for_filter'] = building_art.filter(floor=self.kwargs['floor']).values('categories').order_by('categories')

        # Sets is_floor_in_building to True if the floor in the url is in the building that is in the url, otherwise: False.
        for building in Building_Name.objects.all():
            is_floor_in_building = False
            if building.name.lower() == self.kwargs['building'].lower():
                if self.kwargs['building'].lower() == "all":
                    if int(self.kwargs['floor']) in range(0, 5):    # Range of 0-4 inclusive
                        is_floor_in_building = True
                if int(self.kwargs['floor']) in range(0, building.num_floors + 1):
                    is_floor_in_building = True
                break
        
        context['cfloor_in_cbuilding'] = is_floor_in_building
        context['category_names'] = Category.objects.all().order_by('name')
        context['building_names'] = Building_Name.objects.all().order_by('name')
        
        return context


class BuildingListView(ListView):
    model = Building_Name
    template_name = 'buildings.html'
    context_object_name = 'buildings'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ArtDetailView(DetailView):
    model = Artwork
    template_name = "artwork_detail.html"
    def get_context_data(self, **kwargs):   
        context = super(ArtDetailView, self).get_context_data(**kwargs)
        context['building_names'] = Building_Name.objects.all().order_by('name')
        return context



def map(request):
    building_names = Building_Name.objects.all().order_by('name')
    context = {
        'building_names':building_names
    }
    return render(request, "map.html", context)

def about(request):
    building_names = Building_Name.objects.all().order_by('name')
    context = {
        'building_names':building_names
    }
    return render(request, "about.html", context)

