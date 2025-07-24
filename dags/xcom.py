from airflow.sdk import dag, task, Context

@dag
def x_com_dag():
    
    @task
    def task_a(**context: Context):
        context['ti'].xcom_push(key='my_key', value=val)
        val = 42
    

    @task
    def task_b(context: Context):
        context['ti'].xcom_pull(task_ids='task_a()', key='my_key')
        print(value)

    task_a() >> task_b()

x_com_dag()