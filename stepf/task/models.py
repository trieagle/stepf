from django.db import models
from stepf.account import models as account_models
import datetime


class Task(models.Model):

    title = models.CharField(max_length=100)

    alive = models.IntegerField(default=1)

    owner = models.ForeignKey(account_models.Account)

    create_time = models.DateTimeField(default=datetime.datetime.now)

    #the diary of a task
    diary = models.TextField(blank=True)

    #total steps of a task
    nstep = models.IntegerField()

    #current step
    curr_step = models.IntegerField(default=0)

    #remind user in someday
    frequence = models.IntegerField(default=-1)

    #last update time
    update_time = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.title

    def _update_time(self):
        self.update_time = datetime.datetime.now()

    def update_step(self, stp):
        if stp == 1 and self.curr_step < self.nstep:
            self.curr_step += 1
            msg, created = self.message_set.get_or_create(
                step_id=self.curr_step)
            if not created:
                msg.content = ""
            # CHECK is msg's foreign key setted to self?
            msg.save()
            self._update_time()
            return True
        elif stp == -1 and self.curr_step > 0:
            self.curr_step -= 1
            self._update_time()
            return True
        return False

    def update_total_step(self, stp):
        if stp == 1:
            self.nstep += 1
            return True
        elif stp == -1 and self.nstep > 1 and self.curr_step < self.nstep:
            self.nstep -= 1
            return True

        return False

    # override
    def delete(self, *args, **kwargs):
        self.alive = 0
        self.save()


class Message(models.Model):

    create_time = models.DateTimeField(default=datetime.datetime.now)

    content = models.TextField(blank=True)

    step_id = models.IntegerField()

    owner = models.ForeignKey(Task)
