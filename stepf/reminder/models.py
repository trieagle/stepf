from django.db import models
from stepf.account import models as account_models

import datetime

class Reminder(models.Model):
    
    title = models.CharField(max_length=100)

    alive = models.IntegerField(default=1)

    done = models.IntegerField(default=0)

    owner = models.ForeignKey(account_models.Account);

    create_time = models.DateTimeField(default=datetime.datetime.now)

    alarm_time = models.DateTimeField()

    #picture

    # override
    def delete(self, *args, **kwargs):
        self.alive = 0
        self.save()
