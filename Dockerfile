# Use the official Apache Airflow image as base
FROM apache/airflow:3.0.2-python3.11

# Switch to root user to install system packages
USER root

# Install system dependencies that might be needed for custom operators/hooks
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        curl \
        vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to airflow user
USER airflow

# Copy requirements file for additional Python packages
COPY requirements.txt /tmp/requirements.txt

# Install additional Python packages
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy any custom plugins, DAGs, or configuration files
# COPY --chown=airflow:root ./dags /opt/airflow/dags
# COPY --chown=airflow:root ./plugins /opt/airflow/plugins
# COPY --chown=airflow:root ./config /opt/airflow/config

# Set environment variables for Airflow
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
ENV AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True
ENV AIRFLOW__WEBSERVER__ENABLE_PROXY_FIX=True

# Expose the webserver port
EXPOSE 8080

# The entrypoint and cmd are inherited from the base image
