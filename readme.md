# Flask API Boilerplate

Starter code for making an API using Flask/PostgreSQL.

## What's included at a glance

* **Framework** - Flask
* **Database** - PostgreSQL
* **ORM** - SQLAlchemy
* **Database Migrations** - Alembic
* **Tests** - pytest

## Docker Setup

* Make sure Docker for desktop is running. See [Docker Desktop](https://docs.docker.com/desktop/).
* Run the following command to build and start the containers:

        docker-compose up -d --build

* Stop the containers:

        docker-compose down

* Stop the containers and remove volumes:

        docker-compose down -v

* To view backend logs:

        docker-compose logs -f backend

* To view the database logs:

        docker-compose logs -f database

## Database setup

* Initialize the database (change `db_init.env` as needed first):

        docker-compose run --rm backend python manage.py db init

    **Note:** If you changed the database username or password in `db_init.env` you will also need to update them in the `docker-compose.yml`.

* Create migrations for current models:

        docker-compose run --rm backend python manage.py db migrate

* Apply the migrations:

        docker-compose run --rm backend python manage.py db upgrade

* You can interact with the database via the command line or GUI. See [TablePlus](https://tableplus.com/) for a decent GUI.

## Running the example starter code

* Fire up your favorite API tool. The following commands use [httpie](https://httpie.org/).
* Create a user:

        http POST http://localhost:5000/users username=admin email=admin@admin.com

* Get users:

        http http://localhost:5000/users

