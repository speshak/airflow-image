# DAGs Directory

This directory contains Airflow DAGs (Directed Acyclic Graphs) that define your workflows.

## Example DAG

- `example_dag.py` - Demonstrates the functionality of the custom Airflow image, including testing pandas, requests, and system tools.

## Adding Your Own DAGs

1. Create Python files in this directory
2. Define your DAG using the Airflow DAG class
3. The DAGs will be automatically picked up by Airflow

## Best Practices

- Use descriptive DAG IDs and task IDs
- Add appropriate tags to categorize your DAGs
- Set realistic retry policies
- Use proper error handling in your tasks
- Document your DAGs with docstrings

## Volume Mounting

When running the Docker container, mount this directory to `/opt/airflow/dags`:

```bash
docker run -v $(pwd)/dags:/opt/airflow/dags ghcr.io/speshak/airflow-image:latest
```