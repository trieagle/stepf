from django.db import models
from stepf.account import models as account_models

import datetime

class Reminder(models.Model):
    
    title = models.CharField(max_length=100)

    alive = models.IntegerField()

    done = models.IntegerField()

    owner = models.ForeignKey(account_models.Account);

    create_time = models.DateTimeField(default=datetime.datetime.now)

    alarm_time = models.DateTimeField()

    #picture
