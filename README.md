# Build a Notes App API with Django REST Framework and MongoDB

This repo has the code for my article on [Build a Notes app API with Django REST API and MongoDB](https://www.section.io/engineering-education/django-rest-api-mongodb-notes-app/) which explains how to setup MongoDB database for Django RESTful API projects. A Notes app CRUD API example was used to illustrate the article.

## To Run on Localhost:

- Have `Python` and `pip` installed on your local machine

## Running the Django project:

Create an isolated environment for the project with `virtualenv`. You can install `virtualenv` with the following command:

```
sudo pip install virtualenv
```

Clone the project from GitHub:

```bash
git clone https://github.com/J-rayX/django_mongodb_project
```

Navigate to the cloned project directory:

```
cd django_mongodb_project
```

Create a virtual environment for the project:

```bash
virtualenv venv
```

Then, activate it:

```bash
source venv/bin/activate
```

Install Django and Django REST Framework:

```bash
pip install -r requirements.txt
```

Finally, `cd` into the *notes_app* folder and run the project:

```bash
python manage.py runserver
```

Go to http://localhost:8000/ to see if the API is up and running.

**We move!** 💪
