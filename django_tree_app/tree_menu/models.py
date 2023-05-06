from django.db import models
from django.urls import reverse


class Menu(models.Model):
    menu_name = models.CharField(max_length=50, verbose_name='Название меню')

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):

    label = models.CharField(max_length=30, verbose_name="Название", unique=True)
    url = models.CharField(max_length=200, verbose_name='URL')

    parent = models.CharField(max_length=30, verbose_name="Parent", null=False, blank='no')
    has_children = models.BooleanField(default=False, verbose_name="Имеет подменю")

    position = models.IntegerField(null=False, verbose_name="Позиция")
    menu = models.ForeignKey('Menu', on_delete=models.PROTECT, verbose_name="Меню")

    ordering = ['parent', 'position']

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('show_page', kwargs={'page_slug': self.url})

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'