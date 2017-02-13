import celery
app = celery.Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
@app.task
def hello():
    from time import sleep
    sleep(10)
    return 'hello world'