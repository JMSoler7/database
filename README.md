# database

database research for master thesis

---


## 📝 Prerequisites
Make sure [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/) are installed successfully.

That's all! 🐳


## 🏁 Usage

1. Navigate to database/backend folder. Copy `.env.example` to `.env` and set DJANGO_SETTINGS_MODULE to:
- DJANGO_SETTINGS_MODULE=database.settings.development


2. Navigate to database folder and run:

```bash
make
```

It will:

1) Create Docker images (if not created previously).
2) Run `docker-compose up`, who will launch all Docker containers.


Then you can:

- Visit `http://127.0.0.1:8000` to enter the public view.
- Visit `http://127.0.0.1:8000/admin/` to enter the Django Admin.


If is the first time running the project, you might get an error telling you
something like `[...]relation "django_session" does not exist`. This is because
we need to run Django migrations:

```bash
make init # While Django container is up!
```

Check `Makefile` for additional utility commands.


----


## ✅ Testing
Run the whole test suite (including Jest and Django Test cases):
```bash
make test # same as `make front-test` and `make back-test`
```

----


## 🔨 Using local Django
If you're developing Django, you could prefer to use you local virtual
environment over the default Docker setup.

In order to do that, you can run only Node and Postgre containers with:

```bash
make run-without-django
```

Then, you can start Django in your local virtual environment.


## 🌍 Translating

In order to translate to catalan or spanish you can generate the *.po* files with the respectively commands:

```bash
make translate-ca
make translate-es
```

It will generate a folder called *locale* that will contain folders with each language. Inside them will be a *django.po* file ready to be translated by you. Once upon they are translated, you can compile this translations with:

```bash
make compile-translations
```

It will generate finally *django.mo* files that allow Django to translate in execution time.


#### Considerations:

* You need to install the python module in your environment:
```bash
cd backend/database
pip install -r requirements-dev.txt
```
* Properly set environment variables in order to tell Django how to connect to
the dockerized database and where settings are placed:

```bash
export DJANGO_LOCAL=True
export DJANGO_SETTINGS_MODULE=database.settings.development
```

* All `Makefile` commands are prepared to work with the dockerized Django. If
you're developing with a local Django, you must know the usage of `manage.py`
and execute the commands manually. You can find examples in the `Makefile` or
`docker-compose.yml` files.

___


## 🔨 Debugging external devices
If you're developing on external devices or you want a remote connection to
your docker to be possible you must edit config.js and modify devServer with
your network IP
