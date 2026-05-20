run:
	cd solo_leveling && python manage.py runserver

migrate:
	cd solo_leveling && python manage.py migrate

migrations:
	cd solo_leveling && python manage.py makemigrations

test:
	cd solo_leveling && python manage.py test

lint:
	flake8 ./solo_leveling

format:
	black ./solo_leveling

check: lint format test