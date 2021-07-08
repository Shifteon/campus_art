from django import template
from art.models import Category

register = template.Library()
current_list = []
list_of_floors_displayed = []
last_floor_rendered = 0

@register.filter
def return_last_floor(value):
    return last_floor_rendered

@register.filter
def is_new_floor(current_floor):
    global last_floor_rendered
    if current_floor == 0:
        last_floor_rendered = 0
        return ''

    # if (last_floor_rendered == 0):
    #     last_floor_rendered = current_floor
    if (last_floor_rendered != current_floor):
        last_floor_rendered = current_floor
        return True
    else:
        return False
    # return last_floor_rendered, current_floor

@register.filter
def add_to_list(value):
    # Add code here to check for category objects, then extract name from them. Then add to list. -Kyler
    if value == 0:
        current_list.clear()
    else:
        value_in_list = False
        for x in current_list:
            if x == value:
                value_in_list = True
        if not value_in_list:
            current_list.append(value)
    return("")

@register.filter
def return_list(value):
    # new_list = current_list.sort()
    return(current_list)

# TODO: Remove this tag once we publish this, it is unnecessary.
@register.filter
def return_type(value):
    return type(value)

@register.filter
# Returns name of a category given a dictionary that Django uses.
def get_cat_name(dict):
    value = dict.get('categories')
    category_name = getattr(Category.objects.get(pk=int(value)), 'name')
    return category_name
    # return type is String


@register.filter
def change_category(value, arg):
    first_slash = value.find('/')
    second_slash = value.find('/', first_slash + 1)
    third_slash = value.find('/', second_slash + 1)

    value = value[first_slash:second_slash + 1] + arg + value[third_slash:]
    return value


@register.filter
def change_building(value, category):
    first_slash = value.find('/')
    second_slash = value.find('/', first_slash + 1)

    value = "/" + category + value[second_slash:]
    return value


@register.filter
def int_to_list(num_floors, current_building):
    max_num_floors = 4
    if current_building.lower() == "all":
        return range(0, max_num_floors + 1)
    floors_list = range(0, num_floors + 1)
    return floors_list


@register.filter
def get_current_building(url):
    first_slash = url.find('/')
    second_slash = url.find('/', first_slash + 1)
   
    current_building = url[first_slash + 1:second_slash]
    return current_building.lower()

@register.filter
def get_current_floor(url):
    first_slash = url.find('/')
    second_slash = url.find('/', first_slash + 1)
    third_slash = url.find('/', second_slash + 1)
    fourth_slash = url.find('/', third_slash + 1)

    current_floor = url[third_slash + 1:fourth_slash]
    return int(current_floor)