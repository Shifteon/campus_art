from django import template

register = template.Library()

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