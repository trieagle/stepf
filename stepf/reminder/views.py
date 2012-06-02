#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

from stepf.account.models import Account
from stepf.reminder.models import Reminder

import datetime
import time


_mimetype = 'application/javascript, charset=utf8'

_DEBUG = True

if _DEBUG:
    import pdb
    from stepf.debug_tool import *


def _get_account(user):
    return Account.objects.get(user=user)


def _fetch_reminder_or_ajax_error(request):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    if _DEBUG:
        print simplejson.loads(request.raw_post_data)
    return simplejson.loads(request.raw_post_data)


def create_reminder(request):
    new_reminder = _fetch_reminder_or_ajax_error(request)
    strp_time = time.strptime(new_reminder['alarm_time'], "%Y/%m/%d %H:%M")
    inner_time = datetime.datetime.fromtimestamp(time.mktime(strp_time))
    reminder = Reminder.objects.create(
        title=new_reminder['title'],
        owner=_get_account(request.user),
        alarm_time=inner_time)
    respones = serializers.serialize('json', [reminder])
    return HttpResponse(respones, _mimetype)


@debug_in_out
def remove_reminder(request):
    rm_reminder = _fetch_reminder_or_ajax_error(request)
    try:
        reminder = Reminder.objects.get(id=rm_reminder['id'])
        #FIXME RACE
        reminder.delete()
    except Reminder.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)


@debug_in_out
def done_reminder(request):
    dn_reminder = _fetch_reminder_or_ajax_error(request)
    try:
        reminder = Reminder.objects.get(id=dn_reminder['id'])
        #FIXME RACE
        reminder.done = 1
        reminder.save()
    except Reminder.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)
