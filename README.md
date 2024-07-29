# django-quill-editor

![PyPI](https://img.shields.io/pypi/v/django-quill-editor)

**django-quill-editor** makes [Quill.js](https://quilljs.com/) easy to use on Django Forms and admin sites

- **No configuration required for static files!**
- The entire code for inserting WYSIWYG editor is less than 30 lines
- It can be used in both admin and Django views

![django-quill-editor](https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/master/_assets/django-quill-editor-sample.png)

## Live Demo

#### https://quill.lhy.kr/

- Form | https://quill.lhy.kr/posts/create/normal/
- ModelForm | https://quill.lhy.kr/posts/create/
- Form (Initial HTML) | https://quill.lhy.kr/posts/create/normal/html/
- Form (Initial Text) | https://quill.lhy.kr/posts/create/normal/text/
- Admin | https://quill.lhy.kr/admin/login/



## Documentation

The full document is in [https://django-quill-editor.readthedocs.io/](https://django-quill-editor.readthedocs.io/), including everything about how to use the Form or ModelForm, and where you can add custom settings.

Please refer to the **QuickStart** section below for simple usage.



## QuickStart

### Setup

- Install `django-quill-editor` to your Python environment

  > Requires Python 3.7 or higher and Django 3.1 or higher.

  ```shell
  pip install django-quill-editor
  ```

- Add `django_quill` to `INSTALLED_APPS` in `settings.py`

  ```python
  # settings.py
  INSTALLED_APPS = [
      'django.contrib.admin',
      ...
      'django_quill',
  ]
  ```

### Making Model

Add `QuillField` to the **Model class** you want to use.

> 1. App containing models.py must be added to INSTALLED_APPS
> 2. After adding the app, you need to run makemigrations and migrate to create the DB table.

```python
# models.py
from django.db import models
from django_quill.fields import QuillField

class QuillPost(models.Model):
    content = QuillField()
```

### Using in admin

Just register the Model in **admin.py** of the app.

```python
from django.contrib import admin
from .models import QuillPost

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
```

![admin-sample](https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/master/_assets/admin-sample.png)


## Custom JS and CSS

By default, django-quill-editor uses CDN links for its dependencies. However, you can use your own static files for better control and offline functionality. To do this, you need to define `QUILL_CUSTOM_JS` and `QUILL_CUSTOM_CSS` in your Django settings.

### Required Files

To use custom static files, you need to include the following:

1. Highlight.js (CSS and JS)
2. Quill.js (CSS and JS)
3. Quill Image Compress (JS)
4. Quill Resize Module (JS and CSS)

### Configuration

In your Django `settings.py`, add the following:

```
QUILL_CUSTOM_JS = [
    'path/to/highlight.min.js',
    'path/to/quill.min.js',
    'path/to/quill.imageCompressor.min.js',
    'path/to/quill-resize-module.min.js',
]

QUILL_CUSTOM_CSS = [
    'path/to/highlight-darcula.min.css',
    'path/to/quill.snow.css',
    'path/to/quill-resize.min.css',
]
```
### Using django-npm

Alternatively, you can use [django-npm](https://github.com/kevin1024/django-npm) to manage your static files. Here's how you can set it up:

1. Install django-npm:

```
pip install django-npm
```

2. Add 'django_npm' to your INSTALLED_APPS in settings.py.

3. Configure django-npm in your settings.py:

```
NPM_STATIC_FILES_PREFIX = "vendor"

NPM_FILE_PATTERNS = {
    "quill": ["dist/quill.js", "dist/quill.snow.css"],
    "dropzone": ["dist/dropzone.css"],
    "quill-image-compress/dist/quill.imageCompressor.min.js": ["dist/quill.imageCompressor.min.js"],
    "@highlightjs/cdn-assets": ["highlight.min.js", "styles/darcula.min.css"],
    "@botom/quill-resize-module": [
        "dist/quill-resize-module.min.js",
    ],
}

QUILL_CUSTOM_JS = [
    "vendor/quill-image-compress/dist/quill.imageCompressor.min.js",
    "vendor/@highlightjs/cdn-assets/highlight.min.js",
    "vendor/@botom/quill-resize-module/dist/quill-resize-module.min.js",
    "vendor/quill/dist/quill.js",
]

QUILL_CUSTOM_CSS = [
    "vendor/quill/dist/quill.snow.css",
    "vendor/@highlightjs/cdn-assets/styles/darcula.min.css",
]
```

This setup allows you to use npm packages as static files in your Django project, making it easier to manage and update dependencies.

## Running the Live Demo project in local

The live demo is a deployment of the **"playground"** package, which is a django application within this library.  
After cloning or downloading the repository, you can try running the live demo locally.

**A Python virtual environment is required to run the project.**


# [Optional] We recommend that you start after creating a folder for your project.
mkdir ~/projects
cd projects

# Clone repository
git clone git@github.com:LeeHanYeong/django-quill-editor.git

# Go to the project directory and apply the virtual environment
cd django-quill-editor
# [apply venv]

# Go to the playground package
cd playground

# Install requirements
pip install -r requirements.txt

# Run migrate and runserver
python manage.py migrate
python manage.py runserver


After the above operation, the live demo site works at localhost:8000.

## Contributing

As an open source project, we welcome contributions.
The code lives on [GitHub](https://github.com/LeeHanYeong/django-quill-editor)



## Distribution tips (for owners)

### Installation

```shell
# black
brew install black

# pre-commit
brew install pre-commit
pre-commit install
```

### PyPI Release

```shell
poetry install  # Install PyPI distribution packages
python deploy.py
```

### Sphinx docs

```shell
brew install sphinx-doc  # macOS
```

#### Local

```
cd docs
make html
# ...
# The HTML pages are in _build/html.

cd _build/html
python -m http.server 3001
```

 

### docker-compose up

```shell
# local
docker-compose --env-file .deploy/.env.local up --build --force-recreate --remove-orphans
# production
docker-compose --env-file .deploy/.env.production up --build --force-recreate --remove-orphans
```

