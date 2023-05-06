from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    """
        Main page view function

    """

    context = {
        'title': f'Главная страница сайта',
    }
    return render(request, 'main_site/index.html', context=context)


def show_page(request, page_slug):
    """
        A function for viewing certain pages that are accessible by a slug

    """

    context = {
        'title': f'{page_slug}',
        'page_slug': page_slug
    }

    return render(request, 'main_site/show_page.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
