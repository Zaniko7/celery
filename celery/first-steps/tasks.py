from celery import Celery

app = Celery('tasks')
# app = Celery('tasks', backend='redis://localhost:6379',broker='redis://localhost:6379')
# app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')


app.config_from_object('celeryconfig')

@app.task
def add(x,y):
    return x+y

@app.task
def divide(x,y):
    return x/y