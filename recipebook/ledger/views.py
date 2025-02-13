from django.shortcuts import render
from django.http import HttpResponse

def recipe(request):
	return HttpResponse("Recipe URL")

def list_page(request):
	ctx = {
		"recipes": [
			{
				"name": "Recipe 1",
				"ingredients": [
					{
						"name": "tomato",
						"quantity": "3pcs"
					},
					{
						"name": "onion",
						"quantity": "1pc"
					},
					{
						"name": "pork",
						"quantity": "1kg"
					},
					{
						"name": "water",
						"quantity": "1L"
					},
					{
						"name": "sinigang mix",
						"quantity": "1 packet"
					}
				],
				"link": "/recipe/1"
			},
			{
				"name": "Recipe 2",
				"ingredients": [
					{
						"name": "garlic",
						"quantity": "1 head"
					},
					{
						"name": "onion",
						"quantity": "1pc"
					},
					{
						"name": "vinegar",
						"quantity": "1/2cup"
					},
					{
						"name": "water",
						"quanity": "1 cup"
					},
					{
						"name": "salt",
						"quantity": "1 tablespoon"
					},
					{
						"name": "whole black peppers",
						"quantity": "1 tablespoon"
					},
					{
						"name": "pork",
						"quantity": "1 kilo"
					}
				],
				"link": "/recipe/2"
			}
		]
	}
	return render(request, 'list.html', ctx)

def recipe_page1(request):
	ctx = {
		#^ WIP --> to be replaced with recipe 1 context
		"recipes": [
			{
				"name": "Recipe 1",
				"ingredients": [
					{
						"name": "tomato",
						"quantity": "3pcs"
					},
					{
						"name": "onion",
						"quantity": "1pc"
					},
					{
						"name": "pork",
						"quantity": "1kg"
					},
					{
						"name": "water",
						"quantity": "1L"
					},
					{
						"name": "sinigang mix",
						"quantity": "1 packet"
					}
				],
				"link": "/recipe/1"
			},
			{
				"name": "Recipe 2",
				"ingredients": [
					{
						"name": "garlic",
						"quantity": "1 head"
					},
					{
						"name": "onion",
						"quantity": "1pc"
					},
					{
						"name": "vinegar",
						"quantity": "1/2cup"
					},
					{
						"name": "water",
						"quanity": "1 cup"
					},
					{
						"name": "salt",
						"quantity": "1 tablespoon"
					},
					{
						"name": "whole black peppers",
						"quantity": "1 tablespoon"
					},
					{
						"name": "pork",
						"quantity": "1 kilo"
					}
				],
				"link": "/recipe/2"
			}
		]
	}
	return render(request, 'list.html', ctx)

def recipe_page2(request):
	ctx = {
		#^ WIP --> to be replaced with recipe 2 context
		"recipes": [
			{
				"name": "Recipe 1",
				"ingredients": [
					{
						"name": "tomato",
						"quantity": "3pcs"
					},
					{
						"name": "onion",
						"quantity": "1pc"
					},
					{
						"name": "pork",
						"quantity": "1kg"
					},
					{
						"name": "water",
						"quantity": "1L"
					},
					{
						"name": "sinigang mix",
						"quantity": "1 packet"
					}
				],
				"link": "/recipe/1"
			},
			{
				"name": "Recipe 2",
				"ingredients": [
					{
						"name": "garlic",
						"quantity": "1 head"
					},
					{
						"name": "onion",
						"quantity": "1pc"
					},
					{
						"name": "vinegar",
						"quantity": "1/2cup"
					},
					{
						"name": "water",
						"quanity": "1 cup"
					},
					{
						"name": "salt",
						"quantity": "1 tablespoon"
					},
					{
						"name": "whole black peppers",
						"quantity": "1 tablespoon"
					},
					{
						"name": "pork",
						"quantity": "1 kilo"
					}
				],
				"link": "/recipe/2"
			}
		]
	}
	return render(request, 'list.html', ctx)