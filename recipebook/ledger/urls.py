from django.urls import path

from .views import recipe, list_page

urlpatterns = [
	path('recipe', recipe, name='recipe'),
	path('recipes/list', list_page, name='list_page'),
]

app_name = 'ledger'