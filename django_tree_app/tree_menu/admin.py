from django.contrib import admin
from tree_menu.models import Menu, MenuItem
from tree_menu.forms import AddItemMenuForm


class MenuItemTabular(admin.TabularInline):
    """
        The class defines the display of application fields in the admin panel
    """
    model = MenuItem
    form = AddItemMenuForm

    list_display = ('label', 'parent', 'position', 'has_children', 'url')
    list_display_links = ('label',)
    search_fields = ('parent')
    list_editable = ('position', 'parent', 'has_children', 'url')
    list_filter = ('parent',)
    ordering = ['parent', 'position']

    extra = 0


class MenuItemAdmin(admin.ModelAdmin):
    form = AddItemMenuForm

    list_display = ('label', 'parent', 'position', 'has_children', 'url')
    list_display_links = ('label',)
    search_fields = ('parent',)
    list_editable = ('position', 'parent', 'has_children', 'url')
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
