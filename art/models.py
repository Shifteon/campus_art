from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Model for the name of which building the artwork is in
class Building_Name(models.Model):
    name = models.CharField(max_length=100)
    # Should we add a field that describes the number of floors in that building?
    num_floors = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=1)
    def __str__(self):
        return self.name

# Model for the category of each piece of artwork
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Model for the artist. This model is to reduce redundancy.
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name + " " + self.last_name

# Model for the Artwork includes title, artist name, year created, picture, 
# building and category/categories
class Artwork(models.Model):
    title = models.CharField(max_length=255)
    artist_name = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.CASCADE)
    year_created = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to="pictures/")
    building = models.ManyToManyField('Building_Name', related_name='artwork')
    categories = models.ManyToManyField('Category', related_name='artwork')
    floor = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=1)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title
