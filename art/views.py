from django.shortcuts import render
from .models import Building_Name, Category, Artwork

# An index card version of the artwork
def art_index(request):
    artwork = Artwork.objects.all().order_by('-title')
    context = {
        "artwork": artwork,
    }
    return render(request, "art_index.html", context)

# Artwork organized by building
#Show blog posts in specific category
def art_category(request, category):
    artwork = Artwork.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-title'
    )
    context = {
        "category": category,
        "artwork": artwork
    }
    return render(request, "art_category.html", context)

# Artwork organized by category
def art_building(request, building):
    artwork = Artwork.objects.filter(
        building__name__contains=building
    ).order_by(
        '-title'
    )
    context = {
        "building": building,
        "artwork": artwork
    }
    return render(request, "art_building.html", context)
