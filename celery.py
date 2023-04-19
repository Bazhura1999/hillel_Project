from celery import Celery
import datetime

app = Celery('celery_working', broker='pyamqp://guest@localhost//')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(86400.0, add.s(x=2, y=4), name='add every 10')

@app.task
def add(x, y):
    print(x + y)
    with open('test.txt', 'w') as f:
        f.write(f'x + y = {x + y} {datetime.datetime.now()}')
    return x + y