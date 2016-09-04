import os

from . import BASE_DIR

DATABASES = {  # todo: add customization
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}