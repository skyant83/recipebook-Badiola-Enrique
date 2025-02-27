from django.db import models

# Create your models here.


class Ingredient(models.Model):
    '''Model definition for Ingredient.'''

    name = models.CharField(max_length=255)

    class Meta:
        '''Meta definition for Ingredient.'''

        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('ledger:recipe', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Recipe(models.Model):
    '''Model definition for Recipe.'''

    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('ledger:recipe', kwargs={'pk': self.pk})

    class Meta:
        '''Meta definition for Recipe.'''

        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    '''Model definition for RecipeIngredient.'''

    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe")

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients")

    class Meta:
        '''Meta definition for RecipeIngredient.'''

        verbose_name = 'Recipe Ingredient'
        verbose_name_plural = 'Recipe Ingredients'
