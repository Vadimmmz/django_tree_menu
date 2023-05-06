from django import template
from django.db import connection
from tree_menu.functions import *

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(menu_name):
    """
        Tag function which let build tree-menu using Django possibilities only

    """

    menu_list = list(MenuItem.objects.filter(menu__menu_name=menu_name))
    menu = menu_hierarchy(menu_list)

    # checking that there was only one request to database
    print(connection.queries)

    return {'menu': menu}
