#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from stepf.account.models import Account
from stepf.task.models import Task
from stepf.note.models import Note
from stepf.reminder.models import Reminder
import collections;
import datetime
import calendar

_DEBUG = True

def home(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/index/')

    #FIXME should select undone task
    task_list = Task.objects.filter(
        owner=Account.get_account(request.user),
        alive=1)


    note_list = Note.objects.filter(
        owner=Account.get_account(request.user),
        alive=1,
        done=0)

    reminder_list = Reminder.objects.filter(
        owner=Account.get_account(request.user),
        alive=1,
        done=0)
    if _DEBUG:
        print task_list
        print note_list
        print reminder_list

    return render_to_response("main/index.html",
                              {"username": request.user.username,
                               "task": task_list,
                               "note": note_list,
                               "reminder": reminder_list},
                              context_instance=RequestContext(request))
