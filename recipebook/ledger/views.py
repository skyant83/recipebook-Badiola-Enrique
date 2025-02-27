from django.shortcuts import render

from .models import Recipe


def list_page(req):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
        }
    return render(req, 'recipe_book.html', ctx)


def recipe(req, pk):
    ctx = {
        'recipe': Recipe.objects.get(pk=pk)
    }
    return render(req, 'recipe.html', ctx)
