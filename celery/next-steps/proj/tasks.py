from __future__ import absolute_import, unicode_literals

from .celery import app
import time

@app.task(track_started=True)
def add(x,y):
    time.sleep(15)
    return x+y

@app.task
def divide(x,y):
    time.sleep(15)
    return x/y

@app.task
def average(l):
    return sum(l)/ len(l)