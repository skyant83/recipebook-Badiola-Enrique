from django import forms

from .models import Recipe, RecipeImage, RecipeIngredient


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author']
        label = ['author']


class AddImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['quantity', 'ingredient']
        widgets = {
            'quantity': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'ingredient': forms.Select(attrs={'style': 'width:20ch'})}


IngredientsSet = forms.modelformset_factory(
    RecipeIngredient,
    extra=1,
    min_num=1,
    validate_min=True,
    fields=['quantity', 'ingredient'],
    widgets={
            'quantity': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'ingredient': forms.Select(attrs={'style': 'width:20ch'})}
    )
