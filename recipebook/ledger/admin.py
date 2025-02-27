from django.contrib import admin

from .models import Recipe, RecipeIngredient

# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    '''Inline Admin for RecipeIngredient'''
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    '''Admin View for Recipe'''

    model = Recipe
    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
