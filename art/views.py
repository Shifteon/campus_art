from django.shortcuts import render
from django.views.generic import ListView
from .models import Building_Name, Category, Artwork


class ArtworkListView(ListView):
    model = Artwork
    template_name = 'art_index.html'
    context_object_name = "artwork"     # This is the name of the object that is called in the html file.

# I commented these two list views in preparation for removing the art_building and art_category templates.
# TODO: Delete this commented code when ready to remove the /building/... and /category/... features.
# class ArtCategoryView(ListView):
#     model = Artwork
#     template_name = 'art_category.html'
#     context_object_name = 'artwork'
# 
#     # get_context_data enables us to pass data into the html template. 
#     def get_context_data(self, *args, **kwargs):
#         context = super(ArtCategoryView, self).get_context_data(*args, **kwargs)
#         context['art_context'] = Artwork.objects.filter(categories__name__contains=self.kwargs['category'])     # What does __name__contains mean?
#         context['category_names'] = Category.objects.all()
#         # In self.kwargs['category'], 'category' matches up with the <category> parameter in the urls.py document.
#         return context
# 
# 
# class ArtBuildingView(ListView):
#     model = Artwork
#     template_name = 'art_building.html'
#     context_object_name = 'artwork'
# 
#     def get_context_data(self, **kwargs):   # Do you think it would be possible to give a 404 message if the user navigates to a building that doesn't exist?
#         context = super(ArtBuildingView, self).get_context_data(**kwargs)
#         context['art_context'] = Artwork.objects.filter(building__name__contains=self.kwargs['building'])
#         context['category_names'] = Category.objects.all()
#         return context


class ArtBuildingCategoryView(ListView):
    model = Artwork
    template_name = 'art_building_category.html'
    context_object_name = 'artwork'

    def get_context_data(self, **kwargs):   # Do you think it would be possible to give a 404 message if the user navigates to a building that doesn't exist?
        context = super(ArtBuildingCategoryView, self).get_context_data(**kwargs)
        building_art = Artwork.objects.filter(building__name__contains=self.kwargs['building'])
        context['art_context'] = building_art.filter(categories__name__contains=self.kwargs['category'])

        # context['art_context'] = Artwork.objects.filter(building__name__contains=self.kwargs['building'])
        # context['art_context'] = Artwork.objects.filter(categories__name__contains=self.kwargs['category'])  
        context['category_names'] = Category.objects.all().order_by('name')
        context['building_names'] = Building_Name.objects.all().order_by('name')
        return context

class BuildingListView(ListView):
    model = Building_Name
    template_name = 'buildings.html'
    context_object_name = 'buildings'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


# For the map page
#class CampusMapView(ListView):
#    model = Artwork
#    template_name = 'art_map.html'
#    context_object_name = 'artwork'

def map(request):
    return render(request, "map.html")

