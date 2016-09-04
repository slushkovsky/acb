from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
	'rest_framework',
	'emailusernames',
	'server'
]

AUTHENTICATION_BACKENDS = [
    'emailusernames.backends.EmailAuthBackend'
]


from .redis_sessions  import * 
from .datetime_format import * 
from .international   import *
from .db              import *