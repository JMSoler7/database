DUMP=database.dump

run:
	docker-compose run --rm --service-ports django

run-without-django:
	docker-compose up node db

clean:
	-rm -rf node_modules
	-rm -rf .venv





###############################################################################
### Project initialization
###############################################################################

make-migrations:
	docker-compose run --rm django python manage.py makemigrations

migrate:
	docker-compose run --rm django python manage.py migrate

create-user:
	docker-compose run --rm django \
		bash -c "echo \"from django.contrib.auth import get_user_model; \
		get_user_model().objects.create_superuser('admin', 'admin@example.com', 'admin')\" \
		| python manage.py shell"

init: make-migrations migrate create-user

dropdb:
	docker-compose run --rm psql   dropdb docker

createdb:
	docker-compose run --rm psql   createdb docker

resetdb: dropdb createdb

pg_restore: resetdb
	docker-compose run --rm --volume=`pwd`:/dump psql   pg_restore --dbname=docker --no-owner /dump/$(DUMP)



###############################################################################
### Update dependencies
###############################################################################

front-update-dependencies:
	docker-compose run --rm node npm install --no-audit

back-update-dependencies:
	docker-compose build django

update-dependencies: front-update-dependencies back-update-dependencies





###############################################################################
### Container access
###############################################################################

node:
	docker-compose run --rm node bash

postgres:
	docker-compose run --rm psql

django:
	docker-compose run --rm django python manage.py shell





###############################################################################
### Testing
###############################################################################

front-test:
	docker-compose run --rm node npm test

back-test:
	docker-compose run --rm django python manage.py test

test: front-test back-test





###############################################################################
### Linting
###############################################################################

front-lint:
	docker-compose run --rm --no-deps node npm run lint

back-lint:
	docker-compose run --rm --no-deps django python -m flake8

lint: front-lint back-lint





###############################################################################
### Translations
###############################################################################

translate-ca:
	docker-compose run --rm django python manage.py makemessages -l 'ca'

translate-es:
	docker-compose run --rm django python manage.py makemessages -l 'es'

compile-translations:
	docker-compose run --rm django python manage.py compilemessages