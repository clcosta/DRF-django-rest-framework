run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

adm:
	python __create_super_user.py

check:
	python manage.py check

clean:
	python __clean_files_migrate.py

test:
	python manage.py test