from prefect import flow, task

@task
def my_task():
	print(f'TASK executed')

@flow
def dag():
	print("start")
	for i in range(10):
		my_task()
	print("end")

if __name__ == "__main__":
    dag.from_source(
        source="https://github.com/plipala/prefect_test.git", 
        entrypoint="test_dag.py:dag"
    ).deploy(
        name="dag", 
        work_pool_name="wp", 
    )