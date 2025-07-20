# version 1 -- using PythonOperator

# from airflow.sdk import dag, task, DAG
# from airflow.providers.standard.operators.python import PythonOperator
# from pendulum import datetime

# @dag(
#     schedule = "@daily",
#     start_date = datetime(2025, 7, 20),
#     description = "This dag does ...",
#     tags = ["teamA", "sourceA"],
#     max_consecutive_failed_dag_runs = 3
# ):

# def _task_A():
#     print("Hello from task A!")
    
# def my_dag():
#     task_A = PythonOperator(
#         task_id = "task_A",
#         python_callable = _task_A
#     )

# my_dag()

# version 2 -- using task decorator

from airflow.sdk import dag, task, chain
from pendulum import datetime

@dag(
    schedule = "@daily",
    start_date = datetime(2025, 7, 20),
    description = "This dag does ...",
    tags = ["teamA", "sourceA"],
    max_consecutive_failed_dag_runs = 3
)

def my_dag():

    @task
    def _task_A():
    print("Hello from task A!")

    @task
    def _task_B():
    print("Hello from task B!")

    @task
    def _task_C()):
    print("Hello from task C!")

    @task
    def _task_D():
    print("Hello from task D!")

    @task
    def _task_E():
    print("Hello from task E!")

    task_A() >> task_B() >> task_C() >> task_D() >> task_E()

    # Situation 1: setting up dependencies from task b -- this effectively makes tasks C, D, and E dependent from task B
    # task_A() >> task_B() >> [task_C() , task_D() , task_E()]

    # Situation 2: what if task B and D is dependent on task A, task C dependent on task B, task E dependent on task D?
    # a = task_A ()
    # a >> task_B() >> task_C()
    # a >> task_D() >> task_E()

    # Situation 3: Same as situation 2 but on a single line
    # first you import chain
    # chain(task_A(), [task_B(), task_D()], [task_C(), task_E()])
    
my_dag()
