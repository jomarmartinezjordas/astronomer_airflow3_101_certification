### Using context method

# from airflow.sdk import dag, task, Context

# @dag
# def x_com_dag():
    
#     @task
#     def task_a(**context: Context):
#         context['ti'].xcom_push(key='my_key', value=val)
#         val = 42
    

#     @task
#     def task_b(**context: Context):
#         context['ti'].xcom_pull(task_ids='task_a()', key='my_key')
#         print(value)

#     task_a() >> task_b()

# x_com_dag()

### Better way of push-pull with XComs

# from airflow.sdk import dag, task, Context

# @dag
# def x_com_dag():
    
#     @task
#     def task_a(): # no need to access context
#         val = 42
#         return # xcom_push(key='return_value', val = 42)

#     @task
#     def task_b(val: int):
#         print(val)

#     val = task_a() 
#     task_b(val)

# x_com_dag()

### Another way of push-pull with XComs without using context directly

# from airflow.sdk import dag, task, Context

# @dag
# def x_com_dag():
    
#     @task
#     def task_a(ti: # no need to access context
#         val = 42
#         ti.xcom_push(key='my_key', value = val)

#     @task
#     def task_b(ti):
#         ti.xcom_pull(task_ids='task_a', key="my_key")
#         print(val)

#     task_a() >> task_b()

# x_com_dag()

### Sharing multiple values using XComs

from airflow.sdk import dag, task, Context

@dag
def x_com_dag():
    
    @task
    def task_a(ti: # no need to access context
        val = 42
        ti.xcom_push(key='my_key', value = val)

    @task
    def task_b(ti):
        ti.xcom_pull(task_ids='task_a', key="my_key")
        print(val)

    task_a() >> task_b()

x_com_dag()