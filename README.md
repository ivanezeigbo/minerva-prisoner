# Heroku Django Starter Template

An utterly fantastic project starter template for Django 2.0.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment.

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pipenv install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Heroku Setup

Log into heroku:

    $ heroku login

If you don't have an existing heroku web app created, you can create one with the following command:

    $ heroku create WEBAPP_NAME

To set the remote origin to your web app on heroku, enter the following command:
    
    $ heroku git:remote WEBAPP_NAME

You can also confirm this remote location with the command:

    $ git remote -v
    
It is recommended to have the latest otree version. You can do that with the following command:

    $ pip3 install -U otree

For more info: https://github.com/oTree-org/otree-docs/blob/143a6ab7b61d54ec2be1a8bc09515d78e0b07c71/source/server/heroku.rst#heroku-setup-option-2



## Deployment to Heroku

Ensure that you have updated your Python version in the `runtime.txt` file before you proceed to push to Heroku. This file tells Heroku which Python version to install, else the default version (Python 3.6.10 at the time of writing this README) would be installed.

To check which Python version is installed, enter the command

    $ cat runtime.txt

To deploy heroku, follow the commands below:

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master
    
    $ heroku addons:create heroku-redis:premium-0
    
    $ heroku run "otree resetdb"

    $ heroku open

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
