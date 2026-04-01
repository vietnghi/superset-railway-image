import os
import logging

logger = logging.getLogger()

PYTHONPATH = os.environ.get('PYTHONPATH', '')

RATELIMIT_STORAGE_URI = os.environ.get('SUPERSET_CACHE_REDIS_URL', '')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', '')
SUPERSET_CACHE_REDIS_URL = os.environ.get('SUPERSET_CACHE_REDIS_URL', '')

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": os.environ.get('REDIS_HOST', 'localhost'),
    "CACHE_REDIS_PORT": int(os.environ.get('REDIS_PORT', '6379')),
    "CACHE_REDIS_DB": 0,
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', '')
}
DATA_CACHE_CONFIG = CACHE_CONFIG

class CeleryConfig(object):
    BROKER_URL = os.environ.get('SUPERSET_CACHE_REDIS_URL', '') + "/1"
    CELERY_IMPORTS = ("superset.sql_lab",)
    CELERY_RESULT_BACKEND = os.environ.get('SUPERSET_CACHE_REDIS_URL', '') + "/0"
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

CELERY_CONFIG = CeleryConfig

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))

SUPERSET_ENV = os.environ.get('SUPERSET_ENV', 'development')
SUPERSET_LOAD_EXAMPLES = os.environ.get('SUPERSET_LOAD_EXAMPLES', 'false').lower() == 'true'
SUPERSET_SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY', 'dev-secret-key')
SUPERSET_PORT = os.environ.get('SUPERSET_PORT', '8088')

ENABLE_TEMPLATE_PROCESSING = True

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}
