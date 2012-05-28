#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

from stepf.account.models import Account
from stepf.task.models import Task, Message

_minetype = 'application/javascript, charset=utf8'

def _get_account(user):
    return Account.objects.get(user=user)

def _fetch_task_or_ajax_error(requst):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    return simplejson.loads(request.raw_post_data)

def _fetch_message_or_ajax_error(request):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    return simplejson.loads(request.raw_post_data)

def create_task(request):
    new_task = _fetch_task_or_ajax_error(requst)
    task = Task.objects.create(
        title=new_task['title'],
        owner=_get_account(request.user),
        nstep=new_task['nstep'],
        frequence=new_task['frequence'])

    return HttpResponse(simplejson.dumps(True), _minetype)


def remove_task(request):
    rm_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=rm_task['id'])
        #FIXME ignore race condition
        task.delete()
    except Task.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _minetype)

    return HttpResponse(simplejson.dumps(True), _minetype)


def update_step(request):
    stp_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=stp_task['id'])
        #FIXME ignore race condition
        task.update_step(stp_task['step'])
        task.save()

    except Task.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _minetype)
    
    return HttpResponse(simplejson.dumps(True), _minetype)

def update_title(request):
    tit_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=tit_task['id'])
        #FIXME ignore race condition
        task.title = tit_task['title']
        task.save()
    except Task.DoesNotExist:
        return HttpResponse(simplejson.dump(False), _minetype)

    return HttpResponse(simplejson(True), _minetype))

def update_message(request):
    request_message = _fetch_message_or_ajax_error(request)
    try:
        message = Message.objects.get(id=request_message['id'])
        message.content = request_message['content']
        #FIXME ignore race condition
        message.save()
    except Message.DoesNotExist:
        return HttpResponse(simplejson.dump(False), _minetype)

    return HttpResponse(simplejson(True), _minetype))
