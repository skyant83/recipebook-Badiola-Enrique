from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import AddImageForm, AddRecipeForm, IngredientsSet

from .models import Recipe, RecipeIngredient


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = 'accounts/login'


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_book.html'


class RecipeAddView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'add_recipe.html'
    redirect_field_name = 'accounts/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = AddRecipeForm()
        context['image'] = AddImageForm()
        context['ingredients'] = IngredientsSet(
            queryset=RecipeIngredient.objects.none())

        return context

    def post(self, request, *args, **kwargs):
        recipe_form = AddRecipeForm(request.POST)
        image_form = AddImageForm(request.POST, request.FILES)
        ingredients_form = IngredientsSet(request.POST)

        has_valid_ingredient = any(
            form.cleaned_data for form in ingredients_form if form.is_valid())

        are_forms_valid = (
            recipe_form.is_valid() &
            ingredients_form.is_valid() &
            image_form.is_valid() &
            has_valid_ingredient)

        if are_forms_valid:
            recipe = recipe_form.save()
            for form in ingredients_form:
                if form.cleaned_data:
                    ingredient = form.save(commit=False)
                    ingredient.recipe = recipe
                    ingredient.save()

            image = image_form.save(commit=False)
            image.recipe = recipe
            image.save()

            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['recipe'] = recipe_form
            context['image'] = image_form
            context['ingredients'] = ingredients_form
            return self.render_to_response(context)


class RecipeAddImage(LoginRequiredMixin, FormView):
    form_class = AddImageForm
    template_name = "add_recipe_image.html"
    redirect_field_name = 'accounts/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = AddImageForm()
        return context

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        image = form.save(commit=False)
        image.recipe = recipe
        image.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ledger:recipe', kwargs={'pk': self.kwargs['pk']})
