from django.urls import path

from . import views

urlpatterns = [
    path('recipes/list', views.RecipeListView.as_view(), name='list_page'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add', views.RecipeAddView.as_view(), name='add_recipe'),
    path(
        'recipe/<int:pk>/add_image',
        views.RecipeAddImage.as_view(),
        name='recipe_add_image'),
]

app_name = 'ledger'
