.\.venv\Scripts\activate

py .\\recipebook\\manage.py makemigrations
py .\\recipebook\\manage.py migrate
py .\\recipebook\\manage.py shell -c "from django.contrib.auth.models import User; \
										User.objects.filter(username='admin').exists() or \
										User.objects.create_superuser('admin',
										'', 'admin')"
py .\\recipebook\\manage.py shell -c "exec(open('recipebook\\recipe_filler.py').read())"
deactivate