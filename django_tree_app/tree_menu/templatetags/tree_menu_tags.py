from django import template
from tree_menu.models import MenuItem
from django.db import connection
from pprint import pprint
from tree_menu.functions import *

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(request, menu_name):
    """
        Tag function which let build tree-menu using Django possibilities only

    """

    menu_list = list(MenuItem.objects.filter(menu__menu_name=menu_name))

    # menu = nested_hierarchy(request, menu_list)
    menu = menu_hierarchy(request, menu_list)

    # checking that there was only one request to database
    print(connection.queries)

    return {'menu': menu, 'request': request}