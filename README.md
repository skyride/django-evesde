# django-evesde

Provides models and import system for the EVE fuzzworks SDE. You can use it to build the SDE into your own applications much more easily.

You must have an installation of the fuzzworks SDE available to import. Add it's location as an database within your settings.py with the name "evesde":

~~~
# This database should be a existing version of the fuzzworks SDE
  'evesde': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'sde',
      'HOST': '127.0.0.1',
      'USER': 'user',
      'PASSWORD': 'password',
  },
~~~

After you've migrated the tables, run this command to import the data:

`python manage.py importsde`
