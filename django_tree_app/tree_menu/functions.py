from tree_menu.models import MenuItem


def find_allow_parents(menu_list: list, allowed_parrents: set) -> None:
    """
        This function allow find all parent-entries in current branch
    """

    all_items_checked = False
    for i in menu_list:
        if i.label in allowed_parrents:
            if i.parent not in allowed_parrents and i.parent != 'no':
                allowed_parrents.add(i.parent)

    else:
        if all_items_checked:
            find_allow_parents(menu_list, allowed_parrents)


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


def nested_hierarchy(request, menu_list: list) -> list:
    """
        For building nested-style meny
    """

    current_url = request.path
    current_founded = False
    allowed_parrents = set()
    menu = []

    for i in menu_list:
        match = MenuItem.get_absolute_url(i)
        if match == current_url:
            current_founded = i.label
            allowed_parrents.add(i.label)
            print(match)
            print(current_founded)

    # finding all suitable parents
    find_allow_parents(menu_list, allowed_parrents)
    print(allowed_parrents)

    # finding all suitable entries in database request
    for i in menu_list:
        values = dict()

        if i.label == current_founded:
            values['label'] = i.label
            values['url'] = i.url
            values['parent'] = i.parent
            values['has_children'] = i.has_children
            menu.append(values)

        elif i.parent == 'no':
            values['label'] = i.label
            values['url'] = i.url
            values['parent'] = i.parent
            if i.label in allowed_parrents:
                values['has_children'] = True
            else:
                values['has_children'] = False
            menu.append(values)

        elif i.parent in allowed_parrents:
            values['label'] = i.label
            values['url'] = i.url
            values['parent'] = i.parent
            values['has_children'] = i.has_children
            menu.append(values)
        print(allowed_parrents)

    return menu


def menu_child(current_url: str, menu_list: list, parent: str, menu: list):
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


def menu_hierarchy(request, menu_list: list) -> list:
    """
        For building comment-style meny
    """

    current_url = request.path
    menu = []

    current_founded, allowed_parrents = find_current_url(current_url, menu_list)
    find_allow_parents(menu_list, allowed_parrents)

    no_open = False

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
            print('Текущий: ', i['label'])
            print('parent: ', i['parent'])
            print('allowed_parents: ', allowed_parrents)
            no_open = True
            continue

        if no_open:
            if i['parent'] != current_founded:
                i['has_children'] = False

    return menu
