from django.urls import path

from .views import list_page, recipe_page1, recipe_page2

urlpatterns = [
    path('recipes/list', list_page, name='list_page'),
    path('recipe/1', recipe_page1, name='recipe_page1'),
    path('recipe/2', recipe_page2, name='recipe_page2'),
]

app_name = 'ledger'
