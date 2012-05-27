#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

from stepf.task.models import Task
from stepf.account.models import Account

_minetype = 'application/javascript, charset=utf8'

def _get_account(user):
    return Account.objects.get(user=user)

def _fetch_task_or_ajax_error(reqeust):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    return simplejson.loads(request.raw_post_data)

def create_task(request):
    new_task = _fetch_task_or_ajax_error(reqeust)
    task = Task.objects.create(
        title=new_task['title'],
        owner=_get_account(request.user),
        nstep = new_task['nstep'],
        frequence=new_task['frequence'])

    return HttpResponse(simplejson.dumps(True), _minetype)


def remove_task(request):
    rm_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=rm_task['id'])
        #ignore race condition
        task.remove_self()
        task.save()
    except Task.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _minetype)

    return HttpResponse(simplejson.dumps(True), _minetype)


def do_step(request):
    step_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=step_task['id'])
        #ignore race condition
        task.do_step(step_task['step'])
        task.save()
        return HttpResponse(simplejson.dumps(True), _minetype)
    except Task.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _minetype)

def update_title(request):
    pass

def update_message(request):
    pass
