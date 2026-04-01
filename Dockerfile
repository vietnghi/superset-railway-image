FROM apache/superset:6

USER root

ARG DATABASE_URL

ARG REDISHOST
ARG REDISPORT
ARG REDIS_URL

ARG SUPERSET_SECRET_KEY
ARG SUPERSET_PORT=8088

ENV PYTHONPATH=\"/app/pythonpath:/app/docker/pythonpath_prod\"
ENV REDIS_HOST=\"${REDISHOST}\"
ENV REDIS_PORT=${REDISPORT}
ENV REDIS_URL=\"${REDIS_URL}\"
ENV SUPERSET_CACHE_REDIS_URL=${REDIS_URL}
ENV SUPERSET_ENV=\"production\"
ENV SUPERSET_LOAD_EXAMPLES=\"no\"
ENV SUPERSET_SECRET_KEY=\"${SUPERSET_SECRET_KEY}\"
ENV CYPRESS_CONFIG=False
ENV SUPERSET_PORT=\"${SUPERSET_PORT}\"

ENV SQLALCHEMY_DATABASE_URI=\"${DATABASE_URL}\"
ENV SUPERSET_CONFIG_PATH=/app/docker/superset_config.py

EXPOSE 8088
EXPOSE 5008

# BigQuery support: sqlalchemy-bigquery is the SQLAlchemy dialect;
# db-dtypes is required for BigQuery type handling
# fastmcp is required for the Superset MCP server
RUN pip install sqlalchemy-bigquery db-dtypes google-cloud-bigquery fastmcp

# Specify the startup script as the entry point
COPY startup.sh ./startup.sh
COPY bootstrap.sh /app/docker/docker-bootstrap.sh
COPY superset_config.py superset_config.py

RUN apt-get update
RUN apt-get install gettext -y
RUN envsubst < "superset_config.py" > "/app/docker/superset_config.py"

RUN chmod +x ./startup.sh
RUN chmod +x /app/docker/docker-bootstrap.sh


CMD sh -c "./startup.sh"
#CMD sh -c "./opt/superset/startup.sh"
