from django.db import models
from stepf.account import models as account_models

import datetime

class Task(models.Model):

    title = models.CharField(max_length=100)

    alive = models.IntegerField(default=1)

    owner = models.ForeignKey(account_models.Account);

    create_time = models.DateTimeField(default=datetime.datetime.now)

    #the diary of a task
    diary = models.TextField(blank=True)

    #total steps of a task
    nstep = models.IntegerField()

    #current step
    curr_step = models.IntegerField()

    #remind user in someday
    frequence = models.IntegerField(default=-1) 

    #last update time
    update_time = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.title
    
class Message(models.Model):

    create_time = models.DateTimeField(default=datetime.datetime.now)

    content = models.TextField(blank=True)

    step_id = models.IntegerField();
    
    owner = models.ForeignKey(Task);
