from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    '''Model definition for Profile.'''
    user = models.OneToOneField(User,
                                max_length=50,
                                on_delete=models.CASCADE,
                                verbose_name="Username")
    bio = models.TextField(
        blank=True,
        max_length=255,
        verbose_name="User Bio")

    class Meta:
        '''Meta definition for Profile.'''

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return str(self.user)


class Ingredient(models.Model):
    '''Model definition for Ingredient.'''

    name = models.CharField(max_length=255)

    class Meta:
        '''Meta definition for Ingredient.'''

        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def get_absolute_url(self):
        return reverse('ledger:ingredient', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Recipe(models.Model):
    '''Model definition for Recipe.'''

    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ledger:recipe', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        '''Meta definition for Recipe.'''

        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class RecipeIngredient(models.Model):
    '''Model definition for RecipeIngredient.'''

    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipes")

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients")

    class Meta:
        '''Meta definition for RecipeIngredient.'''

        verbose_name = 'Recipe Ingredient'
        verbose_name_plural = 'Recipe Ingredients'
