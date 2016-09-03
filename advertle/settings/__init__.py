from .base import *

INSTALLED_APPS += [
	'rest_framework',
	'server'
]

from .redis_sessions import * 
from .datetime_format import * 