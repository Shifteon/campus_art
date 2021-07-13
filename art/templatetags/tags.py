from django import template
from art.models import Category

# This file includes template tags for the project. Using template tags, python scripts can run inside our html code.

register = template.Library()
category_list = []
list_of_floors_displayed = []
last_floor_rendered = 0

@register.filter
def return_last_floor(value):
    # Returns the last floor rendered
    return last_floor_rendered

@register.filter
def is_new_floor(current_floor):
    # if value passed in is 0, sets last floor rendered as 0
    global last_floor_rendered
    if current_floor == 0:
        last_floor_rendered = 0
        return ''

    # Returns true if a new floor's artwork is rendered
    if (last_floor_rendered != current_floor):
        last_floor_rendered = current_floor
        return True
    else:
        return False

@register.filter
def add_to_list(value):
    # This function adds the names of categories available in the current building and floor into a list.
    if value == 0:
        category_list.clear()
    else:
        value_in_list = False
        for x in category_list:
            if x == value:
                value_in_list = True
        if not value_in_list:
            category_list.append(value)
    return("")

@register.filter
def return_list(value):
    # Returns list of categories available in the current building and floor.
    return(category_list)

# TODO: Remove this tag once we publish this, it is unnecessary.
@register.filter
def return_type(value):
    # Returns the type of a value. Used for simple debugging.
    return type(value)

@register.filter
# Returns name of a category given a dictionary of category objects.
def get_cat_name(dict):
    value = dict.get('categories')
    category_name = getattr(Category.objects.get(pk=int(value)), 'name')
    return category_name


@register.filter
def change_category(url, category):
    # Given a URL and a category, returns the same URL with a changed category.
    first_slash = url.find('/')
    second_slash = url.find('/', first_slash + 1)
    third_slash = url.find('/', second_slash + 1)

    url = url[first_slash:second_slash + 1] + category + url[third_slash:]
    return url


@register.filter
def int_to_list(num_floors, current_building):
    # This function returns a list of the floors given a building and number of floors for that building.

    # If the building passed into function is 'all', then returns an inclusive range 0-4...
    max_num_floors = 4
    if current_building.lower() == "all":
        floors_list = range(0, max_num_floors + 1)
    # Otherwise, returns an inclusive range of 0-num_floors.
    else:
        floors_list = range(0, num_floors + 1)
    return floors_list


@register.filter
def get_current_building(url):
    # Given a url, returns the building that the user is currently viewing artwork in.
    first_slash = url.find('/')
    second_slash = url.find('/', first_slash + 1)
   
    current_building = url[first_slash + 1:second_slash]
    return current_building.lower()

@register.filter
def get_current_category(url):
    first_slash = url.find('/')
    second_slash = url.find('/', first_slash + 1)
    third_slash = url.find('/', second_slash + 1)

    current_building = url[second_slash + 1:third_slash]
    return current_building.lower()

@register.filter
def get_current_floor(url):
    # Given a url, returns the floor that the user is currently viewing artwork in.
    first_slash = url.find('/')
    second_slash = url.find('/', first_slash + 1)
    third_slash = url.find('/', second_slash + 1)
    fourth_slash = url.find('/', third_slash + 1)

    current_floor = url[third_slash + 1:fourth_slash]
    return int(current_floor)