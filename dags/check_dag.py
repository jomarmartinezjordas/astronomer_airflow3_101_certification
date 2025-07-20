from airflow.sdk import dag, task, chain
from pendulum import datetime

@dag(
    schedule = "@daily",
    start_date = datetime(2025,1,1),
    description = "DAG to check data",
    tags = ["data_engineering"]
)

def check_dag():
    
    @task.bash
    def create_file():
        # First task - creates a file dummy in the tmp directory
        return 'echo "Hi there!" >/tmp/dummy'

    @task.bash
    def check_file():
        # Second task - verifies that the file dummy exists
        return 'test -f /tmp/dummy'
    
    @task
    def read_file():
        # Third task - reads and prints the contents of the file dummy file
        print(open('/tmp/dummy', 'rb').read())

    create_file() >> check_file() >> read_file()

check_dag()