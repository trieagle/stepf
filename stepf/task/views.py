#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

from stepf.account.models import Account
from stepf.task.models import Task, Message


_mimetype = 'application/javascript, charset=utf8'

_DEBUG = True

if _DEBUG:
    from stepf.debug_tool import *


def _get_account(user):
    return Account.objects.get(user=user)


def _fetch_task_or_ajax_error(request):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    return simplejson.loads(request.raw_post_data)


def _fetch_message_or_ajax_error(request):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    return simplejson.loads(request.raw_post_data)


def create_task(request):
    new_task = _fetch_task_or_ajax_error(request)
    if _DEBUG:
        print new_task
        print request.user.username
    task = Task.objects.create(
        title=new_task['title'],
        owner=_get_account(request.user),
        nstep=new_task['nstep'],
        frequence=new_task['frequence'])
    respones = serializers.serialize('json', [task])
    return HttpResponse(respones, _mimetype)


@debug_in_out
def remove_task(request):
    #FIXME check IndexError
    rm_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=rm_task['id'])
        #FIXME RACE
        task.delete()
    except Task.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)


def update_step(request):
    stp_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=stp_task['id'])
        #FIXME RACE
        if not task.update_step(stp_task['step']):
            return HttpResponse(simplejson.dumps(False), _mimetype)
        task.save()

    except Task.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)


def update_title(request):
    tit_task = _fetch_task_or_ajax_error(request)
    try:
        task = Task.objects.get(id=tit_task['id'])
        #FIXME RACE
        task.title = tit_task['title']
        task.save()
    except Task.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)


def update_message(request):
    request_message = _fetch_message_or_ajax_error(request)
    try:
        message = Message.objects.get(id=request_message['id'])
        message.content = request_message['content']
        #FIXME RACE
        message.save()
    except Message.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)
