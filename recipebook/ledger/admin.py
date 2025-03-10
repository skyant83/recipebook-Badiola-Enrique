from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import User
from django.contrib import admin

from .models import Profile, Recipe, RecipeIngredient

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


class RecipeIngredientInline(admin.TabularInline):
    '''Inline Admin for RecipeIngredient'''
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    '''Admin View for Recipe'''

    model = Recipe
    inlines = [RecipeIngredientInline,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
