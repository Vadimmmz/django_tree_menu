from tree_menu.models import MenuItem
from django.http import HttpRequest
from main_site.views import GetRequest


def find_allow_parents(menu_list: list, allowed_parents: set) -> None:
    """
        This function allow find all parent-entries in current branch
    """

    all_items_checked = False
    for i in menu_list:
        if i.label in allowed_parents:
            if i.parent not in allowed_parents and i.parent != 'no':
                allowed_parents.add(i.parent)

    else:
        if all_items_checked:
            find_allow_parents(menu_list, allowed_parents)


def find_current_url(current_url: str, menu_list: list) -> tuple[str, set]:
    """
        This function searches for the active menu item by comparing it with the request URL

    """

    allowed_parrents = set()
    current_founded = False

    for i in menu_list:
        match = MenuItem.get_absolute_url(i)
        if match == current_url:
            current_founded = i.label
            allowed_parrents.add(i.label)
            print(match)
            print(current_founded)

    return current_founded, allowed_parrents


def menu_child(current_url: str, menu_list: list, parent: str, menu: list) -> None:
    """
        Function for building nested items

    """
    for i in menu_list:
        values = dict()
        if i.parent == parent:
            if i.has_children:
                values['label'] = i.label
                values['url'] = i.url
                values['parent'] = i.parent
                values['has_children'] = i.has_children
                menu.append(values)
                menu_child(current_url, menu_list, i.label, menu)
            else:
                values['label'] = i.label
                values['url'] = i.url
                values['parent'] = i.parent
                values['has_children'] = i.has_children
                menu.append(values)


def menu_hierarchy(menu_list: list) -> list:
    """
        For building comment-style meny
    """

    current_url = GetRequest.request
    menu = []

    # Determine active menu item and finding items which should be disclosed
    current_founded, allowed_parrents = find_current_url(current_url, menu_list)
    find_allow_parents(menu_list, allowed_parrents)

    # if True than all next menu-items won't be disclosed
    no_open = False

    # Not open any item if current URL not in menu items URl's
    if not current_founded:
        for i in menu_list:
            values = dict()
            if i.parent == "no":
                values['label'] = i.label
                values['url'] = i.url
                values['parent'] = i.parent
                values['has_children'] = False
                menu.append(values)
        return menu

    # Finding all main menu items and them child-items for each one
    for i in menu_list:
        values = dict()
        if i.parent == "no":
            values['label'] = i.label
            values['url'] = i.url
            values['parent'] = i.parent
            values['has_children'] = i.has_children
            menu.append(values)

            if i.has_children:
                menu_child(current_url, menu_list, i.label, menu)

    for i in menu:
        if i['label'] == current_founded:
            i['current'] = True

            no_open = True
            continue

        # disclosing first nested items before active menu item
        if no_open:
            if i['parent'] != current_founded:
                i['has_children'] = False

    return menu
