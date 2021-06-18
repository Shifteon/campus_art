from django import template

register = template.Library()

@register.filter
def building_change_category(value, arg):
    first_slash = value.find('/')
    second_slash = value.find('/', first_slash + 1)

    value = value[first_slash:second_slash + 1] + arg
    return value

    # TODO: Figure out why the /all/all page does not return paintings with no title


@register.filter
def change_building(value, category):
    first_slash = value.find('/')
    second_slash = value.find('/', first_slash + 1)

    value = "/" + category + value[second_slash:]
    return value


@register.filter
def get_building_name(value, building_name):
    return building_name