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

# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------
MCP_AUTH_ENABLED = os.environ.get('MCP_AUTH_ENABLED', 'false').lower() == 'true'
MCP_DEV_USERNAME = os.environ.get('MCP_DEV_USERNAME', 'admin')

MCP_SERVICE_HOST = os.environ.get('MCP_SERVICE_HOST', '0.0.0.0')
MCP_SERVICE_PORT = int(os.environ.get('MCP_SERVICE_PORT', '5008'))

_mcp_service_url = os.environ.get('MCP_SERVICE_URL', '')
if _mcp_service_url:
    MCP_SERVICE_URL = _mcp_service_url

# Redis-backed SSE session store — required for Railway's stateless containers
MCP_STORE_CONFIG = {
    "enabled": True,
    "CACHE_REDIS_URL": os.environ.get('REDIS_URL', ''),
    "event_store_max_events": 100,
    "event_store_ttl": 3600,
}

MCP_RESPONSE_SIZE_CONFIG = {
    "enabled": True,
    "token_limit": 25000,
    "warn_threshold_pct": 80,
}

# JWT auth (only active when MCP_AUTH_ENABLED=true)
_mcp_jwt_algorithm = os.environ.get('MCP_JWT_ALGORITHM', '')
if _mcp_jwt_algorithm:
    MCP_JWT_ALGORITHM = _mcp_jwt_algorithm

_mcp_jwks_uri = os.environ.get('MCP_JWKS_URI', '')
if _mcp_jwks_uri:
    MCP_JWKS_URI = _mcp_jwks_uri

_mcp_jwt_issuer = os.environ.get('MCP_JWT_ISSUER', '')
if _mcp_jwt_issuer:
    MCP_JWT_ISSUER = _mcp_jwt_issuer

_mcp_jwt_audience = os.environ.get('MCP_JWT_AUDIENCE', '')
if _mcp_jwt_audience:
    MCP_JWT_AUDIENCE = _mcp_jwt_audience

_mcp_jwt_secret = os.environ.get('MCP_JWT_SECRET', '')
if _mcp_jwt_secret:
    MCP_JWT_SECRET = _mcp_jwt_secret
