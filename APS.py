from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.triggers.cron import CronTrigger
import pathlib

executors = {
    'default': ThreadPoolExecutor(20)
}

job_defaults = {
    'coalesce': False, 
    'max_instances': 100
}

path = pathlib.Path("__file__").parent.resolve()
strpath = str(path) + '\jobs.sqlite'
replacement = '\\'
replacement += '\\'
look = '\\'
newpath = ''
for char in strpath:
    if char == look:
        newpath += replacement
    else:
        newpath += char

newpath = 'sqlite:///' + newpath
tz = ""

with open("Timezone.txt", "r") as f:
    tz = f.readlines()[0]

scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults, timezone=tz)
scheduler.configure({'apscheduler.daemon': False})
scheduler.add_jobstore(SQLAlchemyJobStore(url=newpath))
