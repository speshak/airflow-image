"""
Example DAG for the custom Airflow image.
This DAG demonstrates basic functionality and shows that the custom packages are available.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def test_pandas():
    """Test that pandas is available and working."""
    import pandas as pd
    import numpy as np
    
    # Create a simple DataFrame
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'London', 'Tokyo']
    }
    df = pd.DataFrame(data)
    print("Pandas DataFrame created successfully:")
    print(df)
    return df.to_dict()


def test_requests():
    """Test that requests library is available and working."""
    import requests
    
    try:
        # Test with a simple HTTP request
        response = requests.get('https://httpbin.org/get', timeout=10)
        print(f"HTTP request successful. Status code: {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"HTTP request failed: {e}")
        return None


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
dag = DAG(
    'example_custom_image_dag',
    default_args=default_args,
    description='Example DAG for custom Airflow image',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['example', 'custom-image'],
)

# Task to test pandas functionality
test_pandas_task = PythonOperator(
    task_id='test_pandas',
    python_callable=test_pandas,
    dag=dag,
)

# Task to test requests functionality
test_requests_task = PythonOperator(
    task_id='test_requests',
    python_callable=test_requests,
    dag=dag,
)

# Task to test system tools
test_system_tools = BashOperator(
    task_id='test_system_tools',
    bash_command='''
        echo "Testing system tools..."
        echo "Git version: $(git --version)"
        echo "Curl version: $(curl --version | head -1)"
        echo "Vim version: $(vim --version | head -1)"
        echo "Python packages:"
        pip list | grep -E "(pandas|requests)"
    ''',
    dag=dag,
)

# Define task dependencies
test_pandas_task >> test_requests_task >> test_system_tools