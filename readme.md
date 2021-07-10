# Overview
Campus Art is a web application for viewing the artwork contained on the BYU-I campus.
You can search thorugh art by building, floor, and category. Clicking on a picture
allows you to view more information about that specific piece of art.

To run this project on your own machine follow these instructions:
1. Install Python on your machine
2. Run ```pip install django``` (You may need to specify pip version ie. "pip3" if using pip 3)
3. Download the project files
4. Open up your command prompt in the directory you downloaded the files
5. Run ```python manage.py makemigrations``` (You may need to specify python version ie. "python3" if using Python 3)
6. Run ```python manage.py migrate```
7. Run ```python manage.py runserver```<br>
(It should look similar to this)
```
System check identified no issues (0 silenced).
May 20, 2021 - 19:23:40
Django version 3.2.2, using settings 'campus_art.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
8. Open the provided link in your web browser

# Development Environment

* Django
* HTML
* CSS
* JavaScript
* SQLite

# Collaborators

* Kyler Mellor
* Joshua Dean
* Sami Wang
* Benjamin Wyatt
* Kevin Kirby

# Useful Websites

* [Django Docs](https://docs.djangoproject.com/en/3.2/)
* [ArcGIS Docs](https://developers.arcgis.com/documentation/)

# Future Work

* Add more filter options (By artist, Name, etc.)
* Add artwork from more buildings