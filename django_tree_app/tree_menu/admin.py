from django.contrib import admin
from tree_menu.models import Menu, MenuItem
from tree_menu.forms import AddItemMenuForm


class MenuItemTabular(admin.TabularInline):
    """
        Класс определяет отображение полей приложения в админ-панели
    """
    model = MenuItem
    form = AddItemMenuForm

    # Список тех полей, которые мы хотим видеть в админ-панели
    list_display = ('label', 'parent', 'position', 'has_children', 'url')

    # Те поля, на которые мы можем кликнуть и перейти в редактирование
    list_display_links = ('label',)

    # По каким полям мы можем производить поиск
    search_fields = ('parent')

    # Список полей,которые будут редактируемы непосредственно в списке статей админ-панели
    list_editable = ('position', 'parent', 'has_children', 'url')

    # Фильтрация списка в админ-панели
    list_filter = ('parent',)

    ordering = ['parent', 'position']

    extra = 0


class MenuItemAdmin(admin.ModelAdmin):
    form = AddItemMenuForm

    # Список тех полей, которые мы хотим видеть в админ-панели
    list_display = ('label', 'parent', 'position', 'has_children', 'url')

    # Те поля, на которые мы можем кликнуть и перейти в редактирование
    list_display_links = ('label',)

    # По каким полям мы можем производить поиск
    search_fields = ('parent',)

    # Список полей,которые будут редактируемы непосредственно в списке статей админ-панели
    list_editable = ('position', 'parent', 'has_children', 'url')

    # Фильтрация списка в админ-панели
    list_filter = ('parent',)

    ordering = ['parent', 'position']

    extra = 0


class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', )
    list_display_links = ('menu_name', )
    ordering = ['menu_name']

    inlines = [MenuItemTabular]


admin.site.register(Menu, TreeMenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
