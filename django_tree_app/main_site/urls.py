from django.urls import path
from .views import index, show_page

urlpatterns = [
    path('', index, name='home'),
    path('page/<slug:page_slug>', show_page, name='show_page'),
]

