from django.shortcuts import render

# Create your views here.
def building(request):
    numbers = range(1, 20)
    context = {"numbers": numbers}
    return render(request, 'art/building.html', context)