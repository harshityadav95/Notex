# Django Tutorials  

```
sudo apt install python3-pip
pip3 install virtualenv
which virtualenv
virtualenv venv -p python3.6
source venv/bin/activate
pip install django

django-admin startproject myproject

python manage.py runserver



```

- https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html



## Setup

-  Check if you have  the Latest Version of Python 

  ```shell
  python3 --version
  ```

- Install virtualenv environment after installing  pip if you don't have that already  

  ```
  pip install virtualenv
  ```

- Create a folder where you want to setup your project and browse into it and setup a python 3.6  virtualenv inside it 

  ```
  sudo apt install virtualenv
  virtualenv venv -p python3.6
  ```

- Activate the VirtualEnv

  ```
  source venv/bin/activate
  ```

- To Deactivate the env  

  ```
  deactivate
  ```

- Install the Django inside your activated you virtualenv

  ```
   pip install django
  ```

- Start a New Project 

  ```
  django-admin startproject myproject
  
  # which will create the directory structure
  myproject/                  <-- higher level folder
   |-- myproject/             <-- django project folder
   |    |-- myproject/
   |    |    |-- __init__.py
   |    |    |-- settings.py
   |    |    |-- urls.py
   |    |    |-- wsgi.py
   |    +-- manage.py
   +-- venv/                  <-- virtual environment folder
  ```

  

Our initial project structure is composed of five files:

- **manage.py**: a shortcut to use the **django-admin** command-line utility. It’s used to run management commands related to our project. We will use it to run the development server, run tests, create migrations and much more.
- **__init__.py**: this empty file tells Python that this folder is a Python package.
- **settings.py**: this file contains all the project’s configuration. We will refer to this file all the time!
- **urls.py**: this file is responsible for mapping the routes and paths in our project. For example, if you want to show something in the URL `/about/`, you have to map it here first.
- **wsgi.py**: this file is a simple gateway interface used for deployment. You don’t have to bother about it. Just let it be for now.

#### Start your Blank Project

```
python manage.py runserver
```

to create a simple Web Forum or Discussion Board. To create our first app, go to the directory where the **manage.py** file is and executes the following command:

```
django-admin startapp boards

# that will create a strucutre like
myproject/
 |-- myproject/
 |    |-- whiteboard/                <-- our new django app!
 |    |    |-- migrations/
 |    |    |    +-- __init__.py
 |    |    |-- __init__.py
 |    |    |-- admin.py
 |    |    |-- apps.py
 |    |    |-- models.py
 |    |    |-- tests.py
 |    |    +-- views.py
 |    |-- myproject/
 |    |    |-- __init__.py
 |    |    |-- settings.py
 |    |    |-- urls.py
 |    |    |-- wsgi.py
 |    +-- manage.py
 +-- venv/
```

So, let’s first explore what each file does:

- **migrations/**: here Django store some files to keep track of the changes you create in the **models.py** file, so to keep the database and the **models.py** synchronized.
- **admin.py**: this is a configuration file for a built-in Django app called **Django Admin**.
- **apps.py**: this is a configuration file of the app itself.
- **models.py**: here is where we define the entities of our Web application. The models are translated automatically by Django into database tables.
- **tests.py**: this file is used to write unit tests for the app.
- **views.py**: this is the file where we handle the request/response cycle of our Web application.

### STEP 1 :Creating a Hello Word Page for Project

Create the **views.py** file inside the **boards** app, and add the following code:

**views.py** [In the whiteboard project we just created]

```
from django.http import HttpResponse  #add this also

def home(request):
    return HttpResponse('Hello, World!')
```

***urls.py*** [in the other main project folder]

```
from django.conf.urls import url 		#add this 
from django.contrib import admin

from whiteboards import views			#add this

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]

```

***settings.py*** [in the same folder as the urls.py add the following in the Installed apps ]

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'board',
]
```

Now to Run the Project 

```python
python manage.py runserver
```

# Step 2 - Modeling

Since we will be using Sqlite3 as DB , you can use [SQLiteBrowser](https://sqlitebrowser.org/dl/)  as an GUI Interface to browse and edit the DB

### Common field Arguments

The following common arguments can be used when declaring many/most of the different field types:

- [help_text](https://docs.djangoproject.com/en/2.1/ref/models/fields/#help-text): Provides a text label for HTML forms (e.g. in the admin site), as described above.

- [verbose_name](https://docs.djangoproject.com/en/2.1/ref/models/fields/#verbose-name): A human-readable name for the field used in field labels. If not specified, Django will infer the default verbose name from the field name.

- [default](https://docs.djangoproject.com/en/2.1/ref/models/fields/#default): The default value for the field. This can be a value or a callable object, in which case the object will be called every time a new record is created.

- [null](https://docs.djangoproject.com/en/2.1/ref/models/fields/#null): If `True`, Django will store blank values as `NULL` in the database for fields where this is appropriate (a `CharField` will instead store an empty string). The default is `False`.

- [blank](https://docs.djangoproject.com/en/2.1/ref/models/fields/#blank): If `True`, the field is allowed to be blank in your forms. The default is `False`, which means that Django's form validation will force you to enter a value. This is often used with `null=True` , because if you're going to allow blank values, you also want the database to be able to represent them appropriately.

- [choices](https://docs.djangoproject.com/en/2.1/ref/models/fields/#choices): A group of choices for this field. If this is provided, the default corresponding form widget will be a select box with these choices instead of the standard text field. [More on Choices](https://docs.djangoproject.com/en/3.0/topics/db/models/)

- [primary_key](https://docs.djangoproject.com/en/2.1/ref/models/fields/#primary-key): If `True`, sets the current field as the primary key for the model (A primary key is a special database column designated to uniquely identify all the different table records). If no field is specified as the primary key then Django will automatically add a field for this purpose.

  There are many other options — you can view the [full list of field options here](https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-options).

### Common Field Types

The following list describes some of the more commonly used types of fields. 

- [CharField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.CharField) is used to define short-to-mid sized fixed-length strings. You must specify the `max_length` of the data to be stored.

- [TextField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.TextField) is used for large arbitrary-length strings. You may specify a `max_length` for the field, but this is used only when the field is displayed in forms (it is not enforced at the database level).

- [IntegerField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.IntegerField) is a field for storing integer (whole number) values, and for validating entered values as integers in forms.

- [DateField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#datefield) and [DateTimeField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#datetimefield) are used for storing/representing dates and date/time information (as Python `datetime.date` in and `datetime.datetime` objects, respectively). These fields can additionally declare the (mutually exclusive) parameters `auto_now=True` (to set the field to the current date every time the model is saved), `auto_now_add` (to only set the date when the model is first created) , and `default` (to set a default date that can be overridden by the user).

- [EmailField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#emailfield) is used to store and validate email addresses.

- [FileField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#filefield) and [ImageField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#imagefield) are used to upload files and images respectively (the `ImageField` simply adds additional validation that the uploaded file is an image). These have parameters to define how and where the uploaded files are stored.

- [AutoField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#autofield) is a special type of `IntegerField` that automatically increments. A primary key of this type is automatically added to your model if you don’t explicitly specify one.

- [ForeignKey](https://docs.djangoproject.com/en/2.1/ref/models/fields/#foreignkey) is used to specify a one-to-many relationship to another database model (e.g. a car has one manufacturer, but a manufacturer can make many cars). The "one" side of the relationship is the model that contains the "key" (models containing a "foreign key" referring to that "key", are on the "many" side of such a relationship).

  

There are many other types of fields, including fields for different types of numbers (big integers, small integers, floats), booleans, URLs, slugs, unique ids, and other "time-related" information (duration, time, etc.). You can view the [full list here](https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types).

Create the **models.py** file inside the **boards** app, and add the following code:

```
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
```





https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html

https://docs.djangoproject.com/en/3.0/topics/db/models/#

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-options

https://www.journaldev.com/21938/django-models









 