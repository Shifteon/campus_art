from django.contrib import admin
#Added import for models to the admin
from .models import Building_Name,Category,Artwork
# Register your models here.

class Building_NameAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ArtworkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Building_Name, Building_NameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)