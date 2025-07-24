# manual setup of task retries

# @dag(
#     'my_dag', 
#     start_date=datetime(2025, 1 , 1),
#     description='A simple tutorial DAG', 
#     tags=['data_science'],
#     schedule='@daily')

# def my_dag():
    
#     task_a = PythonOperator(task_id='task_a', python_callable=print_a, retries=3)
#     task_b = PythonOperator(task_id='task_b', python_callable=print_b, retries=3)
#     task_c = PythonOperator(task_id='task_c', python_callable=print_c, retries=3)
#     task_d = PythonOperator(task_id='task_d', python_callable=print_d, retries=3)
#     task_e = PythonOperator(task_id='task_e', python_callable=print_e, retries=3)

#     chain(task_a, [task_b, task_c], [task_d, task_e])

# using default_args

default_args = {
    # here you used 'retries' as one default argument to be applied to all tasks
    'retries' : 3,
}

@dag(
    'my_dag', 
    start_date=datetime(2025, 1 , 1),
    description='A simple tutorial DAG', 
    tags=['data_science'],
    schedule='@daily')

def my_dag():

    task_a = PythonOperator(task_id='task_a', python_callable=print_a, retries=3)
    task_b = PythonOperator(task_id='task_b', python_callable=print_b, retries=3)
    task_c = PythonOperator(task_id='task_c', python_callable=print_c, retries=3)
    task_d = PythonOperator(task_id='task_d', python_callable=print_d, retries=3)
    task_e = PythonOperator(task_id='task_e', python_callable=print_e, retries=3)

    chain(task_a, [task_b, task_c], [task_d, task_e])