SESSION_ENGINE = 'redis_sessions.session'

SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PREFIX = 'session'
SESSION_REDIS_SOCKET_TIMEOUT=1

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION' : ['localhost:6380']  # todo: add customization
    },
}