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

Open the **views.py** file inside the **boards** app, and add the following code:

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

```
python manage.py runserver
```

##### Step 2 - Modeling







 