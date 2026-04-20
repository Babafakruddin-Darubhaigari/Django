# Django Calculator Project

This is a small Django beginner project that takes two numbers from a form, adds them, and shows the result on a separate page.

## Features

- Home page with a form for two input numbers
- Result page that displays the sum
- Basic Django app structure using a dedicated `calc` app
- Shared templates with a base layout
- Simple test coverage for the main calculator flow

## Project Structure

```text
my_project/
|-- calc/
|   |-- migrations/
|   |   |-- __init__.py
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- my_project/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- templates/
|   |-- base.html
|   |-- home.html
|   |-- result.html
|-- README.md
|-- manage.py
|-- requirements.txt
```

Note: `__pycache__`, virtual environment folders, and `db.sqlite3` are local/generated files and are not meant to be committed.

## How It Works

- [my_project/urls.py](./my_project/urls.py) connects the `calc` app to the main project.
- [calc/urls.py](./calc/urls.py) defines the calculator routes.
- [calc/views.py](./calc/views.py) contains the page logic.
- [templates/home.html](./templates/home.html) shows the form.
- [templates/result.html](./templates/result.html) shows the calculated result.
- [calc/tests.py](./calc/tests.py) contains basic tests for the home page and add flow.

## Requirements

- Python 3.12+
- Packages listed in [requirements.txt](./requirements.txt)

## Setup

1. Create a virtual environment:

```powershell
python -m venv venv
```

2. Activate the virtual environment:

```powershell
venv\Scripts\Activate.ps1
```

3. Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

4. Apply Django migrations:

```powershell
python manage.py migrate
```

## Run The Project

Start the development server:

```powershell
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Run Tests

```powershell
python manage.py test
```

## URLs

- `/` shows the home page
- `/add/` calculates and displays the result
- `/admin/` opens the Django admin panel

## Notes

- The calculator currently uses a `GET` request to submit the form.
- The `add` view now handles invalid input and shows a friendly message instead of crashing.
- Templates are loaded from the top-level `templates` folder.
- The root project file wires the app through `include('calc.urls')`, while the calculator logic itself lives inside the `calc` app.

## Learning Purpose

This project is a good starting point for learning:

- Django URL routing
- Function-based views
- Template inheritance
- Form handling with request data
