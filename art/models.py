from django.db import models

# Create your models here.
<<<<<<< HEAD
=======

# Model for the name of which building the artwork is in
class Building_Name(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Model for the category of each piece of artwork
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Model for the Artwork includes title, artist name, year created, picture, 
# building and category/categories
class Artwork(models.Model):
    title = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=55)
    year_created = models.IntegerField()
    picture = models.ImageField(upload_to="pictures/")
    building = models.ManyToManyField('Building_Name', related_name='artwork')
    categories = models.ManyToManyField('Category',related_name='artwork')
>>>>>>> e99d7ae0937b439555fef499770cc18157befbf4
