import os

from . import BASE_DIR

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'), 
    ('en', 'English')
)

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ   = True