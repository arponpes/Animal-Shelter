[![Coverage Status](https://coveralls.io/repos/github/arponpes/Animal-Shelter/badge.svg?branch=feat%2Ftest)](https://coveralls.io/github/arponpes/Animal-Shelter?branch=feat%2Ftest)
[![Build Status](https://travis-ci.org/arponpes/Animal-Shelter.svg?branch=master)](https://travis-ci.org/arponpes/Animal-Shelter)

# Animal-Shelter
Front page and administrator of an animal shelter.

## Demo

* [Animal Shelter](https://animal-shelter-vigo.herokuapp.com/)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

* Python
* Npm
* Pipenv
* Postgres

### Installing

```
createdb shelter
pipenv shell
pipenv install --dev
pytohn manage.py makemigrations
pytohn manage.py migrate
python manage.py collectstatic
npm install bulma
pytohn manage.py runserver
```

## Running the tests

```
pytest
```

## Authors

* **Aaron Domginuez** - *Initial work* - [aronpes](https://github.com/arponpes)

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details

### Documentación


* [django](https://docs.djangoproject.com/en/2.0/)
* [Bulma](https://bulma.io/documentation/overview/start/)
* [boto3](http://boto3.readthedocs.io/en/latest/)
* [pytest](https://docs.pytest.org/en/latest/)
* [pytest-selenium](pytest-selenium.readthedocs.io/en/latest/user_guide.html)
* [travis](https://docs.travis-ci.com/)
* [coveralls](https://docs.coveralls.io/)
* [heroku](https://devcenter.heroku.com/)
* [django-versatileimagefield](https://django-versatileimagefield.readthedocs.io/en/latest/)
* [factory-boy](http://factoryboy.readthedocs.io/en/latest/)
