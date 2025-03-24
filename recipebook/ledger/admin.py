from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Profile, Recipe, RecipeImage, RecipeIngredient

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


class RecipeIngredientInline(admin.TabularInline):
    '''Inline Admin for RecipeIngredient'''
    model = RecipeIngredient
    extra = 1


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    '''Admin View for Recipe'''

    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
