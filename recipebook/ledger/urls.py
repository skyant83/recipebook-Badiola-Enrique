from django.urls import path

from .views import list_page, recipe

urlpatterns = [
    path('recipes/list', list_page, name='list_page'),
    path('recipe/<int:pk>', recipe, name='recipe'),
]

app_name = 'ledger'
