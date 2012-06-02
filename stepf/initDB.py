from stepf.task.models import *
from stepf.note.models import *
from stepf.reminder.models import *
from stepf.account.models import *
from django.contrib.auth.models import User
import datetime

## generate user: eagle
username = "tester"
email = "tester@example.com"
password = "tester"
user_obj = User.objects.create_user(username,email,password)
user_obj.save()
tester = Account.objects.create(user=user_obj)
    
## generate task:task1,task2,task3

task1 = Task.objects.create(title='Keep on stepf', owner=tester, nstep = 4, curr_step=0, frequence=2)
task2 = Task.objects.create(title='Prepare for youdao nanti competition', owner=tester, nstep = 10, curr_step=3, frequence=1)
task3 = Task.objects.create(title='Read django rel books', owner=tester, nstep = 2, curr_step=0, frequence=4)

## generate note:note1,note2,note3

note1 = Note.objects.create(title='Participate aliyun activity', owner=tester)
note2 = Note.objects.create(title='Read paper one', owner=tester)
note3 = Note.objects.create(title='Process bar', owner=tester)

## generate reminder:reminder1,reminder2,reminder3

reminder1 = Reminder.objects.create(title='Go to lib next thursday', owner=tester, alarm_time=datetime.datetime(2012,6,3,10,2))
reminder2 = Reminder.objects.create(title='Check for update', owner=tester, alarm_time=datetime.datetime(2012,6,10,10,2))
reminder1 = Reminder.objects.create(title='Go to lab', owner=tester, alarm_time=datetime.datetime(2012,6,1,10,2))


