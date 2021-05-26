from django.shortcuts import render
from django.views.generic import ListView
from .models import Building_Name, Category, Artwork

# An index card version of the artwork
# def art_index(request):
#     artwork = Artwork.objects.all().order_by('-title')
#     context = {
#         "artwork": artwork,
#     }
#     return render(request, "art_index.html", context)

class ArtworkListView(ListView):
    model = Artwork
    template_name = 'art_index.html'
    context_object_name = "artwork"     # This is the name of the object that is called in the html file.

# Artwork organized by building
#Show artwork posts in specific category
# def art_category(request, category):
#     artwork = Artwork.objects.filter(
#         categories__name__contains=category
#     ).order_by(
#         '-title'
#     )
#     context = {
#         "category": category,
#         "artwork": artwork
#     }
#     return render(request, "art_category.html", context)

class ArtCategoryView(ListView):
    model = Artwork
    template_name = 'art_category.html'
    context_object_name = 'artwork'

    # get_context_data enables us to pass data into the html template. 
    def get_context_data(self, *args, **kwargs):
        context = super(ArtCategoryView, self).get_context_data(*args, **kwargs)
        context['art_context'] = Artwork.objects.filter(categories__name__contains=self.kwargs['category'])     # What does __name__contains mean?
        # In self.kwargs['category'], 'category' matches up with the <category> parameter in the urls.py document.
        return context


# Artwork organized by category
# def art_building(request, building):
#     artwork = Artwork.objects.filter(
#         building__name__contains=building
#     ).order_by(
#         '-title'
#     )
#     numbers = range(0, 20) # this is for testing
#     context = {
#         "building": building,
#         "artwork": artwork,
#         "numbers": numbers
#     }
#     return render(request, "art_building.html", context)

class ArtBuildingView(ListView):
    model = Artwork
    template_name = 'art_building.html'
    context_object_name = 'artwork'

    def get_context_data(self, **kwargs):   # Do you think it would be possible to give a 404 message if the user navigates to a building that doesn't exist?
        context = super(ArtBuildingView, self).get_context_data(**kwargs)
        context['art_context'] = Artwork.objects.filter(building__name__contains=self.kwargs['building'])
        return context
