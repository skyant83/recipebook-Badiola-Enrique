from ledger.models import Ingredient, Recipe, RecipeIngredient


context = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": 3
                },
                {
                    "name": "onion",
                    "quantity": 1
                },
                {
                    "name": "pork",
                    "quantity": 1
                },
                {
                    "name": "water",
                    "quantity": 1
                },
                {
                    "name": "sinigang mix",
                    "quantity": 1
                }
            ]
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": 1
                },
                {
                    "name": "onion",
                    "quantity": 1
                },
                {
                    "name": "vinegar",
                    "quantity": 1
                },
                {
                    "name": "water",
                    "quantity": 1
                },
                {
                    "name": "salt",
                    "quantity": 1
                },
                {
                    "name": "whole black peppers",
                    "quantity": 1
                },
                {
                    "name": "pork",
                    "quantity": 1
                }
            ]
        }
    ]
}

for recipe in context["recipes"]:
    recipe = Recipe()
    recipe.name = recipe["name"]
    recipe.save()

    for ingredient in recipe["ingredients"]:
        ingredient = Ingredient()
        ingredient.name = ingredient["name"]
        ingredient.save()

        recipe_ingredient = RecipeIngredient()
        recipe_ingredient.quantity = ingredient["quantity"]
        recipe_ingredient.recipe = recipe
        recipe_ingredient.ingredient = ingredient
        recipe_ingredient.save()
