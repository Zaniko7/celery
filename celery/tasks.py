from celery import Celery

# app = Celery('tasks', broker='redis://localhost:6379')
app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

@app.task
def add(x,y):
    return x+y