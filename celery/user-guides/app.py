from celery import Celery


app = Celery('app')

app.config_from_object('celeryconfig')

@app.task(name='app.helloworld')
def helloworld():
    return 'helloworld'
app = Celery()
print(app)