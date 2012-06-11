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
def overview_note(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/index/')

    note_in_process = Note.objects.filter(
        owner=Account.get_account(request.user),
        alive=1,
        done=0)
    
    note_done = Note.objects.filter(
        owner=Account.get_account(request.user),
        alive=0,
        done=1)

    note_deleted = Note.objects.filter(
        owner=Account.get_account(request.user),
        alive=0,
        done=0)

    if _DEBUG:
        print note_in_process

    return render_to_response("main/note/note_overview.html",
                              {"username": request.user.username,
                               "note_in_process": note_in_process,
                               "note_done": note_done,
                               "note_deleted": note_deleted},
                              context_instance=RequestContext(request))
def overview_task(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/index/')
    
    tasks = Task.objects.filter(
        owner=Account.get_account(request.user),)
    
    task_in_process = [v for v in tasks if v.alive and v.curr_step < v.nstep]

    task_done = [v for v in tasks if v.alive and v.curr_step >= v.nstep]

    task_deleted = [v for v in tasks if not v.alive]

    if _DEBUG:
        print task_in_process

    return render_to_response("main/task/task_overview.html",
                              {"username": request.user.username,
                               "task_in_process": task_in_process,
                               "task_done": task_done,
                               "task_deleted": task_deleted},
                              context_instance=RequestContext(request))

def overview_reminder(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/index/')

    reminder_in_process = Reminder.objects.filter(
        owner=Account.get_account(request.user),
        alive=1,
        done=0)
    
    reminder_done = Reminder.objects.filter(
        owner=Account.get_account(request.user),
        alive=0,
        done=1)

    reminder_deleted = Reminder.objects.filter(
        owner=Account.get_account(request.user),
        alive=0,
        done=0)

    if _DEBUG:
        print reminder_in_process

    return render_to_response("main/reminder/reminder_overview.html",
                              {"username": request.user.username,
                               "reminder_in_process": reminder_in_process,
                               "reminder_done": reminder_done,
                               "reminder_deleted": reminder_deleted},
                              context_instance=RequestContext(request))

