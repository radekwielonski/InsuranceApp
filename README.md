# InsuranceApp

Application to store insurance data

## Description

Application backend is written in python with django and django rest framework.

## Built with

### Backend

- [Python](https://www.python.org/) - Language
- [Django](https://www.djangoproject.com/) - Web framework
- [DRF](https://www.django-rest-framework.org/) - REST Web Services

## Installation

## Installation

#### Clone repository:

```sh
$ git clone https://github.com/radekwielonski/InsuranceApp
```

#### Create virtual environment:

```sh
$ python -m venv venv
```

#### Activate virtual environment:

```sh
$ source venv/bin/activate
```

#### Upgrade pip:

```sh
$ python -m pip install --upgrade pip
```

#### Install requirements:

```sh
$ pip install -r requirements.txt
```

#### Change directory to main project path:

```sh
$ cd InsuranceApp
```

#### Create DB:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Run django:

```sh
$ python manage.py runserver
```

#### GET REST api links:

```sh
$ http://127.0.0.1:8000/api/v1/
```
